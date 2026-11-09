# DevOps & Virtualization Lab — WSKZ

<div align="center">

**Koło Naukowe Nowoczesnej Infrastruktury IT, Wirtualizacji i Bezpieczeństwa**  
*Wyższa Szkoła Kształcenia Zawodowego (WSKZ)*

[![Status](https://img.shields.io/badge/Status-Aktywne-0969da?style=flat-square)](https://github.com/wskz-devops-lab)
[![Portal WWW](https://img.shields.io/badge/Portal_WWW-strona--kola-10b981?style=flat-square)](https://wskz-devops-lab.github.io/strona-kola/)
[![Platforma](https://img.shields.io/badge/Infrastruktura-Proxmox_VE_&_OpenNebula-d9381e?style=flat-square)](https://github.com/wskz-devops-lab/architektura-proxmox)
[![Dokumentacja](https://img.shields.io/badge/Docs-Baza_Wiedzy_(MkDocs)-1a7f37?style=flat-square)](https://wskz-devops-lab.github.io/materialy-dydaktyczne/)

</div>

---

## Profil Koła Naukowego

DevOps & Virtualization Lab zrzesza studentów oraz pasjonatów zainteresowanych administracją systemami, automatyzacją wdrożeń, konteneryzacją oraz niezależną infrastrukturą chmurową. Działalność koła koncentruje się na praktycznych warsztatach, realizacji projektów laboratoryjnych oraz badaniach nad wydajnością i bezpieczeństwem systemów zwirtualizowanych.

### Główne obszary techniczne i badawcze:
1. **Wirtualizacja i zarządzanie zasobami:** KVM, QEMU, Proxmox VE, OpenNebula, obrazy bazowe (Golden Image) oraz klonowanie dowiązane (Linked Clones / Copy-on-Write).
2. **Konteneryzacja i orkiestracja:** Docker, Podman (rootless), Kubernetes (k3s), GitOps (ArgoCD) oraz separacja środowisk uruchomieniowych.
3. **Automatyzacja i CI/CD:** Podejście Infrastructure as Code (OpenTofu / Terraform), automatyzacja konfiguracji z wykorzystaniem Ansible, potoki testowania i walidacji kodu.
4. **Prywatna infrastruktura i self-hosting:** Prywatne chmury danych (Nextcloud, OnlyOffice), systemy backupu przyrostowego 3-2-1 (BorgBackup, Restic), bezpieczne sieci nakładkowe VPN (WireGuard, Tailscale).
5. **Wdrożenia modeli sztucznej inteligencji:** Uruchamianie i optymalizacja modeli językowych (Ollama, vLLM, llama.cpp), techniki Retrieval-Augmented Generation (RAG), GPU Passthrough (VFIO) oraz rozproszona brama Campus AI Gateway (LiteLLM).
6. **Cyberbezpieczeństwo i audyty systemowe:** Hardening systemów Linux, audyty podatności wirtualizacji (Red Teaming — 5 filarów ochrony), segmentacja sieciowa, ochrona brzegu sieci (WAF, Reverse Proxy, CrowdSec) oraz systemy detekcji (Suricata, Cowrie, Wazuh).

---

## Repozytoria Organizacji

Ekosystem koła podzielony jest na dedykowane repozytoria zadaniowe:

| Repozytorium | Widoczność | Opis merytoryczny |
| :--- | :---: | :--- |
| **[`strona-kola`](https://github.com/wskz-devops-lab/strona-kola)** | Publiczne | Oficjalny portal internetowy koła naukowego ([wskz-devops-lab.github.io/strona-kola](https://wskz-devops-lab.github.io/strona-kola/)). |
| **[`materialy-dydaktyczne`](https://github.com/wskz-devops-lab/materialy-dydaktyczne)** | Publiczne | Dokumentacja techniczna w modelu Docs-as-Code ([MkDocs](https://wskz-devops-lab.github.io/materialy-dydaktyczne/)) — instrukcje wdrożeniowe i katalog 16 projektów laboratoryjnych. |
| **[`architektura-proxmox`](https://github.com/wskz-devops-lab/architektura-proxmox)** | Publiczne | Uniwersalna architektura wirtualizacji, klastrów i laboratoriów na Proxmox VE (Track A): KVM, LXC (nesting), ZFS/Ceph, SDN, GPU Passthrough, IaC. |
| **[`architektura-vdi-opennebula`](https://github.com/wskz-devops-lab/architektura-vdi-opennebula)** | Publiczne | Suwerenna architektura chmurowa VDI na OpenNebula i AlmaLinux 9 (Track B): klonowanie CoW, orkiestracja Ansible/Terraform, portal laboratoryjny. |
| **[`pakiet-red-teaming`](https://github.com/wskz-devops-lab/pakiet-red-teaming)** | Publiczne | Narzędzie automatyzacji audytu bezpieczeństwa, weryfikujące izolację wirtualizacji w 5 kluczowych filarach ochrony. |
| **[`klaster-gpu-ai`](https://github.com/wskz-devops-lab/klaster-gpu-ai)** | Publiczne | Rozproszony klaster GPU AI i brama Campus AI Gateway (Ollama, LiteLLM, Open WebUI) [W rozwoju]. |

---

## Wybór Projektu i Formularze Zgłoszeń (Issues)

Każdy członek koła realizuje wybrany projekt laboratoryjny (z katalogu **01–16** lub temat autorski) w dedykowanym repozytorium wewnątrz organizacji `wskz-devops-lab`. Bot koła może automatycznie założyć repozytorium i nadać uprawnienia administratora po wypełnieniu formularza.

* **[FORMULARZE ISSUES]** [**Otwórz ekran wyboru formularza zgłoszeniowego (Issues)**](https://github.com/wskz-devops-lab/.github/issues/new/choose)  
  Dostępne szablony zgłoszeń:
  1. **`[PROJEKT] Zgłoszenie projektu studenckiego / Inkubator`** — wybór tematu `01–16` lub własnego projektu i automatyczne założenie repozytorium ([link bezpośredni](https://github.com/wskz-devops-lab/.github/issues/new?template=01_zgloszenie_projektu.yml)).
  2. **`[DOCS / LAB] Nowe ćwiczenie lub poradnik do Bazy Wiedzy`** — propozycja instrukcji do MkDocs.
  3. **`[INFRA / IaC] Moduł infrastruktury lub automatyzacja`** — zadanie wdrożenia kodu Ansible / Terraform / Docker.
  4. **`[SEC / RED-TEAM] Test audytu bezpieczeństwa lub reguła detekcji`** — nowy test dla 5 filarów ochrony lub SIEM/WAF.
  5. **`[BUG] Błąd w konfiguracji, skrypcie lub środowisku laboratoryjnym`** — zgłoszenie problemu technicznego.
* **[PRZEWODNIK]** [**Instrukcja dla studentów krok po kroku (Git, SSH, Inkubator projektów)**](https://github.com/wskz-devops-lab/.github/blob/main/INSTRUKCJA_DLA_STUDENTOW.md)

---

## Organizacja i Komunikacja

* **Portal Koła i Dobór Ścieżki:** [wskz-devops-lab.github.io/strona-kola](https://wskz-devops-lab.github.io/strona-kola/)
* **Baza Wiedzy (Projekty 01–16 i Poradniki):** [wskz-devops-lab.github.io/materialy-dydaktyczne](https://wskz-devops-lab.github.io/materialy-dydaktyczne/)
* **Zulip:** Podstawowa platforma wymiany informacji technicznych oraz wideokonferencji (indywidualne zaproszenie przesyła opiekun koła drogą mailową).
* **Spotkania laboratoryjne:** Zdalne warsztaty praktyczne oraz demonstracje środowisk realizowane w cyklu dwutygodniowym bezpośrednio w Zulipie (zapasowo: Nextcloud Talk).
* **Konsultacje projektowe:** Dyżury merytoryczne i przeglądy postępów prac zespołowych (rezerwacja w kalendarzu chmury).

---

<div align="center">
<sub>Koło Naukowe DevOps & Virtualization Lab · Wyższa Szkoła Kształcenia Zawodowego</sub>
</div>
