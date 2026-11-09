#!/usr/bin/env python3
"""
Automatyczna obsługa zgłoszenia projektu studenckiego w organizacji wskz-devops-lab.
- Weryfikuje członkostwo studenta w organizacji
- Pobiera preferencje widoczności (Private / Dla członków koła / Public)
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
            f"Cześć @{issue_user},\n\n"
            f"Zgłoszenia w Inkubatorze projektowym organizacji **{org}** "
            f"są dostępne wyłącznie dla przyjętych członków Koła Naukowego WSKZ.\n\n"
            f"Jeśli jesteś studentem WSKZ i chcesz dołączyć do koła, wypełnij formularz zgłoszeniowy "
            f"na stronie koła lub skontaktuj się z opiekunem koła drogą mailową, aby otrzymać zaproszenie do organizacji."
        )
        run_cmd(["gh", "issue", "comment", issue_number, "-R", f"{org}/.github", "-b", msg])
        run_cmd(["gh", "issue", "close", issue_number, "-R", f"{org}/.github"])
        print(f"Użytkownik {issue_user} nie jest członkiem koła. Issue #{issue_number} zamknięte.")
        sys.exit(0)

    # 1a. Upewnij się, że członek koła należy do zespołu "studenci" (idempotentne)
    if issue_user.lower() != "pzarnecki":
        run_cmd(["gh", "api", "-X", "PUT", f"orgs/{org}/teams/studenci/memberships/{issue_user}", "-f", "role=member"], check=False)

    # 2. Parsowanie odpowiedzi z formularza Issue
    def extract_field(header):
        pattern = rf"### {header}\s*\n+([^\n#]+)"
        match = re.search(pattern, issue_body, re.IGNORECASE)
        return match.group(1).strip() if match else ""

    project_choice = extract_field("Wybierz projekt lub ścieżkę")
    repo_create_mode = extract_field("Automatyczne utworzenie repozytorium przez bota")
    repo_visibility = extract_field("Widoczność repozytorium projektu")
    repo_keyword = extract_field("Krótkie słowo kluczowe do nazwy repozytorium (opcjonalnie)")

    # 3. Wyznaczenie słowa kluczowego do nazwy repozytorium (pełne pokrycie Projektów 01–16 + Własny)
    if repo_keyword and repo_keyword.lower() not in ("_brak odpowiedzi_", "_no response_"):
        slug = re.sub(r"[^a-zA-Z0-9_-]", "", repo_keyword.lower().replace(" ", "-"))
    else:
        c = project_choice.lower()
        if "projekt 01" in c or "wirtualizacja firmowego" in c:
            slug = "wirtualizacja-kvm"
        elif "projekt 02" in c or "konteneryzacja" in c or "s1" in c:
            slug = "konteneryzacja-docker"
        elif "projekt 03" in c or "automatyczny build" in c or "ci/cd" in c:
            slug = "cicd-automation"
        elif "projekt 04" in c or "prywatna chmura" in c or "nextcloud" in c:
            slug = "prywatna-chmura"
        elif "projekt 05" in c or "backup" in c:
            slug = "backup-system"
        elif "projekt 06" in c or "opennebula" in c:
            slug = "opennebula-iaas"
        elif "projekt 07" in c or "klaster wirtualizacji proxmox" in c:
            slug = "proxmox-cluster"
        elif "projekt 08" in c or "kubernetes" in c or "k3s" in c:
            slug = "kubernetes-k3s"
        elif "projekt 09" in c or "monitoring" in c or "s4" in c:
            slug = "monitoring-grafana"
        elif "projekt 10" in c or "arm" in c or "raspberry" in c:
            slug = "platforma-arm"
        elif "projekt 11" in c or "serwer ai" in c or "ollama" in c or "s3" in c:
            slug = "serwer-ai-llm"
        elif "projekt 12" in c or "węzeł brzegowy" in c or "wezel brzegowy" in c or "waf" in c or "s2" in c:
            slug = "brama-waf-vpn"
        elif "projekt 13" in c or "segmentacja sieci" in c:
            slug = "segmentacja-sieci"
        elif "projekt 14" in c or "szyfrowanie" in c or "sekret" in c:
            slug = "szyfrowanie-sekrety"
        elif "projekt 15" in c or "ipfs" in c:
            slug = "rozproszone-ipfs"
        elif "projekt 16" in c or "red teaming" in c or "honeypot" in c or "s5" in c:
            slug = "security-redteam"
        else:
            slug = "homelab"

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
        repo_exists = run_cmd(["gh", "repo", "view", f"{org}/{repo_name}"], check=False).returncode == 0

        if not repo_exists:
            create_res = run_cmd(["gh", "repo", "create", f"{org}/{repo_name}", vis_flag, "--clone=false", "--add-readme"], check=False)

            if create_res.returncode == 0:
                run_cmd(["gh", "api", "-X", "PUT", f"repos/{org}/{repo_name}/collaborators/{issue_user}", "-f", "permission=admin"], check=False)
                if share_with_team:
                    run_cmd(["gh", "api", "-X", "PUT", f"orgs/{org}/teams/studenci/repos/{org}/{repo_name}", "-f", "permission=pull"], check=False)

                comment = (
                    f"### [OK] Repozytorium projektu utworzone dla @{issue_user}\n\n"
                    f"Twoje repozytorium laboratoryjne zostało automatycznie skonfigurowane w organizacji **`{org}`**.\n\n"
                    f"* **Wybrany temat:** `{project_choice}`\n"
                    f"* **Adres repozytorium:** [**github.com/{org}/{repo_name}**](https://github.com/{org}/{repo_name})\n"
                    f"* **Widoczność:** `{vis_desc}`\n"
                    f"* **Twoje uprawnienia:** `Admin` (pełny dostęp do gałęzi, tagów i ustawień repozytorium)\n\n"
                    f"#### Kolejne kroki techniczne:\n"
                    f"1. **Sklonuj repozytorium na komputer roboczy:**\n"
                    f"   ```bash\n"
                    f"   git clone git@github.com:{org}/{repo_name}.git\n"
                    f"   cd {repo_name}\n"
                    f"   ```\n"
                    f"2. **Rozpocznij pracę:** uzupełnij `README.md` o cel i architekturę rozwiązania, dodaj pliki konfiguracyjne (`compose.yaml`, skrypty, playbooki) oraz plik `.gitignore`.\n"
                    f"3. **Konsultacje i pytania:** niniejszy wątek (Issue #{issue_number}) służy do bieżącej dyskusji nad projektem i zgłaszania postępów."
                )
            else:
                comment = (
                    f"### [INFO] Wymagane ręczne utworzenie repozytorium dla @{issue_user}\n\n"
                    f"Wystąpił błąd podczas automatycznego zakładania repozytorium: `{create_res.stderr.strip()}`.\n"
                    f"Możesz utworzyć je bezpośrednio pod adresem: https://github.com/organizations/{org}/repositories/new "
                    f"podając nazwę: `{repo_name}`."
                )
        else:
            comment = (
                f"### [INFO] Repozytorium już istnieje (@{issue_user})\n\n"
                f"Repozytorium [**{org}/{repo_name}**](https://github.com/{org}/{repo_name}) jest już dostępne w organizacji.\n"
                f"Możesz od razu kontynuować w nim pracę."
            )
    else:
        # Tryb manualny
        comment = (
            f"### [PROJEKT] Zarejestrowano zgłoszenie projektu dla @{issue_user}\n\n"
            f"* **Wybrany temat:** `{project_choice}`\n\n"
            f"#### Kolejne kroki (tryb samodzielnego utworzenia repozytorium):\n"
            f"1. **Utwórz swoje repozytorium w organizacji:**\n"
            f"   * Przejdź do: https://github.com/organizations/{org}/repositories/new\n"
            f"   * Jako **Owner** wybierz organizację `{org}`\n"
            f"   * Zalecana nazwa repozytorium: **`{repo_name}`**\n"
            f"   * Widoczność: **`{vis_desc}`**\n"
            f"   * Zaznacz utworzenie pliku `README.md`\n"
            f"2. **Wklej link do repozytorium w komentarzu poniżej.**\n"
            f"3. **Sklonuj repozytorium lokalnie i rozpocznij pracę.**"
        )

    run_cmd(["gh", "issue", "comment", issue_number, "-R", f"{org}/.github", "-b", comment])
    print(f"Pomyślnie przetworzono zgłoszenie #{issue_number} dla @{issue_user}.")

if __name__ == "__main__":
    main()
