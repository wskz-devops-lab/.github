#!/usr/bin/env python3
"""
Automatyczna obsługa zgłoszenia projektu studenckiego w organizacji wskz-devops-lab.
- Weryfikuje członkostwo studenta w organizacji
- Pobiera preferencje widoczności (Private / Internal / Public)
- Na życzenie studenta automatycznie tworzy repozytorium w organizacji
- Nadaje studentowi uprawnienia administratora do jego repozytorium
- Odpowiada w Issue z podsumowaniem i instrukcją kolejnych kroków
"""

import os
import re
import subprocess
import sys

def run_cmd(cmd, check=True):
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if check and res.returncode != 0:
        print(f"Błąd komendy: {' '.join(cmd)}\nSTDERR: {res.stderr}", file=sys.stderr)
    return res

def main():
    issue_number = os.environ.get("ISSUE_NUMBER")
    issue_user = os.environ.get("ISSUE_USER", "").strip()
    issue_body = os.environ.get("ISSUE_BODY", "")
    
    if not issue_number or not issue_user:
        print("Brak ISSUE_NUMBER lub ISSUE_USER.")
        sys.exit(0)

    org = "wskz-devops-lab"

    # 1. Sprawdzenie członkostwa w organizacji wskz-devops-lab
    check_member = run_cmd(["gh", "api", f"orgs/{org}/members/{issue_user}"], check=False)
    is_member = (check_member.returncode == 0)

    if not is_member:
        # Sprawdź, czy ma zaproszenie oczekujące
        check_invites = run_cmd(["gh", "api", f"orgs/{org}/invitations", "--jq", ".[].login"], check=False)
        if issue_user.lower() in [login.lower() for login in check_invites.stdout.split()]:
            is_member = True

    if not is_member and issue_user.lower() != "pzarnecki":
        msg = (
            f"Cześć @{issue_user}! 👋\n\n"
            f"Dziękujemy za zainteresowanie! Zgłoszenia w Inkubatorze projektowym organizacji **{org}** "
            f"są dostępne wyłącznie dla przyjętych członków Koła Naukowego WSKZ.\n\n"
            f"Jeśli jesteś studentem WSKZ i chcesz dołączyć do koła, wypełnij formularz zgłoszeniowy "
            f"lub skontaktuj się z opiekunem koła drogą mailową, aby otrzymać oficjalne zaproszenie."
        )
        run_cmd(["gh", "issue", "comment", issue_number, "-R", f"{org}/.github", "-b", msg])
        run_cmd(["gh", "issue", "close", issue_number, "-R", f"{org}/.github"])
        print(f"Użytkownik {issue_user} nie jest członkiem koła. Issue #{issue_number} zamknięte.")
        sys.exit(0)

    # 2. Parsowanie odpowiedzi z formularza Issue
    def extract_field(header):
        pattern = rf"### {header}\s*\n+([^\n#]+)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        return match.group(1).strip() if match else ""

    project_choice = extract_field("Wybierz projekt lub ścieżkę")
    repo_create_mode = extract_field("Automatyczne utworzenie repozytorium przez bota")
    repo_visibility = extract_field("Widoczność repozytorium projektu")
    repo_keyword = extract_field("Krótkie słowo kluczowe do nazwy repozytorium (opcjonalnie)")

    # 3. Wyznaczenie słowa kluczowego do nazwy repozytorium
    if repo_keyword and repo_keyword.lower() != "_brak odpowiedzi_":
        slug = re.sub(r"[^a-zA-Z0-9_-]", "", repo_keyword.lower().replace(" ", "-"))
    else:
        c = project_choice.lower()
        if "s1" in c or "docker" in c or "homelab" in c:
            slug = "homelab-docker"
        elif "s2" in c or "wireguard" in c or "tailscale" in c:
            slug = "vpn-access"
        elif "s3" in c or "ai" in c or "ollama" in c:
            slug = "ai-server"
        elif "s4" in c or "monitoring" in c or "prometheus" in c:
            slug = "monitoring"
        elif "s5" in c or "wazuh" in c or "cyberbezpiecze" in c:
            slug = "security-lab"
        elif "01" in c or "wirtualizacja" in c:
            slug = "kvm-wirtualizacja"
        elif "03" in c or "cicd" in c:
            slug = "cicd-automation"
        elif "04" in c or "chmura" in c:
            slug = "private-cloud"
        elif "05" in c or "backup" in c:
            slug = "backup-lab"
        elif "06" in c or "opennebula" in c:
            slug = "opennebula-vdi"
        elif "07" in c or "proxmox" in c:
            slug = "proxmox-cluster"
        elif "08" in c or "kubernetes" in c or "k3s" in c:
            slug = "k8s-cluster"
        elif "16" in c or "red teaming" in c:
            slug = "red-teaming"
        else:
            slug = "projekt-lab"

    repo_name = f"projekt-{slug}-{issue_user}".lower()

    # 4. Ustalenie widoczności
    # Plan GitHub Free nie obsługuje repozytoriów "internal" — "dla członków koła"
    # realizujemy jako repozytorium prywatne z prawem odczytu dla zespołu "studenci".
    share_with_team = False
    vis_lower = repo_visibility.lower()
    if "członków koła" in vis_lower or "czlonkow kola" in vis_lower:
        vis_flag = "--private"
        vis_desc = "Dla członków koła (prywatne + odczyt dla zespołu Studenci)"
        share_with_team = True
    elif "publiczne" in vis_lower:
        vis_flag = "--public"
        vis_desc = "Publiczne (Public — widoczne w internecie)"
    else:
        vis_flag = "--private"
        vis_desc = "Prywatne (Private — dostęp masz tylko Ty i opiekun)"

    # 5. Tworzenie repozytorium (jeśli wybrano automatyczne tworzenie)
    if "tak" in repo_create_mode.lower():
        # Sprawdź czy repo już istnieje
        repo_exists = run_cmd(["gh", "repo", "view", f"{org}/{repo_name}"], check=False).returncode == 0
        
        if not repo_exists:
            # Tworzenie repozytorium
            create_res = run_cmd(["gh", "repo", "create", f"{org}/{repo_name}", vis_flag, "--clone=false", "--add-readme"], check=False)

            if create_res.returncode == 0:
                # Nadanie studentowi uprawnień Admin do jego repozytorium
                run_cmd(["gh", "api", "-X", "PUT", f"repos/{org}/{repo_name}/collaborators/{issue_user}", "-f", "permission=admin"], check=False)
                if share_with_team:
                    run_cmd(["gh", "api", "-X", "PUT", f"orgs/{org}/teams/studenci/repos/{org}/{repo_name}", "-f", "permission=pull"], check=False)
                
                comment = (
                    f"🎉 Cześć @{issue_user}!\n\n"
                    f"Twoje repozytorium laboratoryjne zostało **automatycznie utworzone** przez bota koła! 🚀\n\n"
                    f"👉 **Adres repozytorium:** [**github.com/{org}/{repo_name}**](https://github.com/{org}/{repo_name})\n"
                    f"* **Widoczność:** `{vis_desc}`\n"
                    f"* **Twoje uprawnienia:** Administrator (masz pełną swobodę tworzenia gałęzi, tagów i konfiguracji)\n\n"
                    f"### 📋 Jak zacząć pracę:\n"
                    f"1. **Sklonuj repozytorium na swój komputer:**\n"
                    f"   ```bash\n"
                    f"   git clone git@github.com:{org}/{repo_name}.git\n"
                    f"   cd {repo_name}\n"
                    f"   ```\n"
                    f"2. **Dodaj pierwsze pliki:** zaktualizuj `README.md`, dodaj pliki konfiguracyjne (`compose.yaml`, skrypty, playbooki) i zrób push.\n"
                    f"3. **Konsultacje i pytania:** ten wątek (Issue #{issue_number}) służy do bieżącej dyskusji nad Twoim projektem. Pytaj śmiało o wszystko!\n\n"
                    f"Powodzenia w realizacji! 💪"
                )
            else:
                comment = (
                    f"Cześć @{issue_user}! 👋\n\n"
                    f"Wystąpił problem przy automatycznym tworzeniu repozytorium: `{create_res.stderr.strip()}`.\n"
                    f"Możesz założyć je ręcznie pod adresem: https://github.com/organizations/{org}/repositories/new "
                    f"podając nazwę: `{repo_name}`."
                )
        else:
            comment = (
                f"Cześć @{issue_user}! 👋\n\n"
                f"Repozytorium [**{org}/{repo_name}**](https://github.com/{org}/{repo_name}) już istnieje w organizacji!\n"
                f"Możesz od razu kontynuować w nim swoją pracę."
            )
    else:
        # Tryb manualny
        comment = (
            f"Cześć @{issue_user}! 👋\n\n"
            f"Dzięki za zgłoszenie wyboru projektu do Inkubatora Koła Naukowego WSKZ!\n\n"
            f"### 📋 Twoje kolejne kroki:\n"
            f"1. **Utwórz swoje repozytorium w organizacji:**\n"
            f"   * Przejdź do: https://github.com/organizations/{org}/repositories/new\n"
            f"   * Jako **Owner** upewnij się, że wybrana jest organizacja `{org}`\n"
            f"   * Proponowana nazwa repozytorium: **`{repo_name}`**\n"
            f"   * Wybierz widoczność: **`{vis_desc}`**\n"
            f"   * Zaznacz dodanie pliku `README.md`\n"
            f"2. **Wklej link do repozytorium w komentarzu poniżej.**\n"
            f"3. **Sklonuj repozytorium na komputer i rozpocznij pracę.**\n\n"
            f"W razie wątpliwości pytaj w komentarzach poniżej lub na Zulipie!"
        )

    run_cmd(["gh", "issue", "comment", issue_number, "-R", f"{org}/.github", "-b", comment])
    print(f"Pomyślnie przetworzono zgłoszenie #{issue_number} dla @{issue_user}.")

if __name__ == "__main__":
    main()
