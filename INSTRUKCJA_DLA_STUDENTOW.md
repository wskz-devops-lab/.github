# Przewodnik Członka Koła Naukowego — DevOps & Virtualization Lab (WSKZ)

Witaj w **DevOps & Virtualization Lab** przy Wyższej Szkole Kształcenia Zawodowego.  
Niniejszy przewodnik wyjaśnia krok po kroku organizację pracy na GitHubie, wybór projektu z katalogu **01–16** oraz zasady tworzenia repozytoriów i oddawania zmian.

---

## Krok 1: Konto i narzędzia komunikacji

### 1. Komunikacja i spotkania (Zulip)
Głównym centrum komunikacji technicznej i spotkań warsztatowych koła jest **Zulip**.
* **Dostęp do platformy:** Imienne zaproszenie do przestrzeni Zulip otrzymasz od opiekuna koła na adres e-mail podany w formularzu rekrutacyjnym.
* Po dołączeniu przedstaw się w kanale ogólnym i napisz, które obszary z katalogu projektów najbardziej Cię interesują (wirtualizacja Proxmox/OpenNebula, kontenery Docker/K8s, IaC Ansible/Terraform, lokalne AI czy cyberbezpieczeństwo).
* **Spotkania online:** Warsztaty odbywają się bezpośrednio na Zulipie w wątku **`spotkania online`** (zapasowo wykorzystywany jest pokój w Nextcloud Talk).

### 2. GitHub i Zespół Studenci
* Otrzymasz zaproszenie do organizacji **`wskz-devops-lab`**.
* Po zaakceptowaniu zaproszenia Twoje konto jest automatycznie dodawane do zespołu **`@wskz-devops-lab/studenci`**.
* Skonfiguruj klucz SSH na swoim koncie GitHub ([Oficjalna dokumentacja GitHub SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)).

---

## Krok 2: Wybór projektu i automatyczne utworzenie repozytorium (Inkubator)

W kole każdy uczestnik (indywidualnie, w parze lub w małym zespole) realizuje wybrany projekt laboratoryjny. Lista tematów w formularzu Issues jest w 100% zgodna z katalogiem na **[Stronie WWW Koła](https://wskz-devops-lab.github.io/strona-kola/#projekty)** oraz w **[Bazie Wiedzy MkDocs](https://wskz-devops-lab.github.io/materialy-dydaktyczne/projekty/katalog-projektow-1-16/)**.

### 1. Katalog 16 Projektów Laboratoryjnych (01–16) + Projekt Własny
Projektom polecanym osobom zaczynającym od podstaw przypisano oznaczenie **`[START]`**:

* **Projekt 01 `[START / ŚREDNI]`:** Wirtualizacja firmowego środowiska roboczego (Proxmox VE, KVM/QEMU, snapshoty)
* **Projekt 02 `[START]`:** Konteneryzacja małej usługi biznesowej (Docker, Podman, Docker Compose)
* **Projekt 03 `[ŚREDNI]`:** Automatyczny build po zmianach w repozytorium (CI/CD, GitHub Actions, Ansible)
* **Projekt 04 `[START / ŚREDNI]`:** Prywatna chmura i własny office — Self-Hosting (Nextcloud, OnlyOffice, Reverse Proxy)
* **Projekt 05 `[START / ŚREDNI]`:** System backupu przyrostowego i odtwarzania 3-2-1 (Restic, BorgBackup, szyfrowanie)
* **Projekt 06 `[START / ŚREDNI]`:** Suwerenna chmura IaaS — OpenNebula & AlmaLinux 9 (KVM, Copy-on-Write, Terraform)
* **Projekt 07 `[ŚREDNI]`:** Klaster wirtualizacji Proxmox VE — KVM, LXC, Ceph/ZFS i Rolling Upgrade
* **Projekt 08 `[ŚREDNI / ZAAW.]`:** Lokalny klaster Kubernetes i wdrożenie usługi (k3s, ArgoCD, GitOps)
* **Projekt 09 `[ŚREDNI]`:** Monitoring usług i reakcja na awarie — Green Computing & DCGM (Prometheus, Grafana)
* **Projekt 10 `[START / ŚREDNI]`:** Mini-platforma usługowa na urządzeniu ARM (Raspberry Pi, Linux, Docker, VPN)
* **Projekt 11 `[START -> ZAAW.]`:** Własny serwer AI i klaster GPU — modele LLM, RAG, VFIO i LiteLLM (Ollama, Open WebUI)
* **Projekt 12 `[ŚREDNI]`:** Bezpieczny węzeł brzegowy — reverse proxy, TLS, WAF i dostęp VPN (Caddy, Traefik, WireGuard, CrowdSec)
* **Projekt 13 `[ŚREDNI / ZAAW.]`:** Segmentacja sieci i automatyczna reakcja na atak (VLAN, nftables, Suricata, CrowdSec)
* **Projekt 14 `[ŚREDNI]`:** Szyfrowanie danych i zarządzanie sekretami (LUKS, TLS, age, SOPS, HashiCorp Vault, YubiKey)
* **Projekt 15 `[ŚREDNI / ZAAW.]`:** Rozproszone przechowywanie danych — IPFS i analiza prywatności (Kubo, swarm key, age)
* **Projekt 16 `[START -> ZAAW.]`:** Laboratorium bezpieczeństwa — analiza ruchu, honeypot i Red Teaming (Wireshark, Suricata, Cowrie, Wazuh)
* **Projekt Własny `[AUTORSKI]`:** Własny pomysł na projekt / homelab / zagadnienie ze środowiska zawodowego

### 2. Zgłoś projekt w Issues (automatyczne założenie repozytorium)
1. Otwórz bezpośrednio: 👉 **[Formularz zapisu na projekt (01–16)](https://github.com/wskz-devops-lab/.github/issues/new?template=01_zgloszenie_projektu.yml)** (lub przejdź do [ekranu wyboru wszystkich formularzy Issues](/../../issues/new/choose)).
2. Wybierz z listy swój projekt (`01–16` lub `Projekt Własny`), wskaż preferowaną widoczność repozytorium (`Prywatne`, `Dla członków koła` lub `Publiczne`) oraz zaznacz opcję **automatycznego utworzenia repozytorium przez bota**.
3. Po wysłaniu zgłoszenia bot koła w ciągu kilkudziesięciu sekund:
   * utworzy w organizacji repozytorium `projekt-<temat>-<twoj_login>`,
   * nada Ci uprawnienia administratora (`Admin`) do tego repozytorium,
   * zamieści w komentarzu pod Twoim Issue bezpośredni link oraz komendy `git clone`.

*(Alternatywnie możesz zaznaczyć w formularzu tryb ręczny i samodzielnie kliknąć `New repository` w organizacji `wskz-devops-lab`).*

---

## Krok 3: Praca z kodem (Git Workflow)

W repozytoriach wspólnych koła stosujemy standardowy przepływ pracy z gałęziami (branch workflow).

### 1. Sklonuj repozytorium na komputer roboczy
```bash
git clone git@github.com:wskz-devops-lab/NAZWA_REPOZYTORIUM.git
cd NAZWA_REPOZYTORIUM
```

### 2. Utwórz gałąź roboczą (branch)
```bash
# Dla nowej funkcji lub instrukcji:
git checkout -b feat/instrukcja-wireguard-proxmox

# Dla poprawki błędu:
git checkout -b fix/korekta-konfiguracji-compose
```

### 3. Wprowadź zmiany i przetestuj je
* Dokumentacja (MkDocs): zweryfikuj podgląd lokalnie (`mkdocs serve`).
* Skrypty i konfiguracja (Docker, Ansible, Terraform): przetestuj działanie na maszynie wirtualnej lub kontenerze.

### 4. Bezpieczeństwo i higiena repozytorium
Przed wykonaniem commita upewnij się, że:
* W repozytorium **nie znajdują się żadne hasła, tokeny API, pliki `.env` z sekretami ani klucze prywatne SSH (`id_rsa`)**.
* Wrażliwe parametry są zastąpione zmiennymi środowiskowymi lub plikami przykładowymi (`.env.example`).

### 5. Zatwierdź i wyślij zmiany
```bash
git add .
git commit -m "feat(docs): dodano instrukcję konfiguracji WireGuarda w kontenerze LXC"
git push -u origin feat/instrukcja-wireguard-proxmox
```

---

## Krok 4: Pull Request i Code Review (w projektach wspólnych)

1. Po wypchnięciu gałęzi na GitHuba kliknij przycisk **`Compare & pull request`**.
2. Wypełnij krótki szablon opisu PR i zaznacz wykonane punkty listy kontrolnej.
3. Jeśli zmiana dotyczy konkretnego zgłoszenia w Issues, dopisz np. `Closes #12`.
4. Kliknij **`Create pull request`** i daj znać na Zulipie w odpowiednim wątku projektowym.

---

## Krok 5: Pozostałe formularze zgłoszeń w Issues

Na ekranie wyboru **[New Issue (`/issues/new/choose`)](https://github.com/wskz-devops-lab/.github/issues/new/choose)** oprócz zgłoszenia projektu studenckiego dostępne są jeszcze 4 wyspecjalizowane formularze techniczne (w każdym formularzu możesz też przełączyć szablon przyciskiem **`Change template`** u góry strony):

1. **`[PROJEKT] Zapis na projekt z listy 16 tematów (lub własny pomysł)`** — wybór tematu `01–16` lub własnego projektu ([otwórz formularz](https://github.com/wskz-devops-lab/.github/issues/new?template=01_zgloszenie_projektu.yml)).
2. **`[DOCS / LAB] Nowe ćwiczenie lub poradnik do Bazy Wiedzy`** — propozycja nowej instrukcji do repozytorium `materialy-dydaktyczne`.
3. **`[INFRA / IaC] Moduł infrastruktury lub automatyzacja`** — propozycja playbooka Ansible, modułu Terraform lub konfiguracji klastra.
4. **`[SEC / RED-TEAM] Test audytu bezpieczeństwa lub reguła detekcji`** — nowy scenariusz testowy dla 5 filarów bezpieczeństwa lub reguła WAF/SIEM.
5. **`[BUG] Błąd w konfiguracji, skrypcie lub środowisku laboratoryjnym`** — zgłoszenie błędu w dowolnym repozytorium organizacji.
