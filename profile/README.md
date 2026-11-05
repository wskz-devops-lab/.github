# DevOps & Virtualization Lab — WSKZ

<div align="center">

**Koło Naukowe Nowoczesnej Infrastruktury IT, Wirtualizacji i Bezpieczeństwa**  
*Wyższa Szkoła Kształcenia Zawodowego (WSKZ)*

[![Status](https://img.shields.io/badge/Status-Aktywne-0969da?style=flat-square)](https://github.com/wskz-devops-lab)
[![Platforma](https://img.shields.io/badge/Infrastruktura-Proxmox_VE_8.x-d9381e?style=flat-square)](https://proxmox.com)
[![Dokumentacja](https://img.shields.io/badge/Docs-Baza_Wiedzy-1a7f37?style=flat-square)](https://github.com/wskz-devops-lab/materialy-dydaktyczne)

</div>

---

## Profil Koła Naukowego

DevOps & Virtualization Lab zrzesza studentów oraz pasjonatów zainteresowanych administracją systemami, automatyzacją wdrożeń, konteneryzacją oraz niezależną infrastrukturą chmurową. Działalność koła koncentruje się na praktycznych warsztatach, realizacji projektów laboratoryjnych oraz badaniach nad wydajnością i bezpieczeństwem systemów zwirtualizowanych.

### Główne obszary techniczne i badawcze:
1. **Wirtualizacja i zarządzanie zasobami:** KVM, QEMU, Proxmox VE, obrazy bazowe (Golden Image) oraz klonowanie dowiązane (Linked Clones / Copy-on-Write).
2. **Konteneryzacja i orkiestracja:** Docker, Podman (rootless), Kubernetes, mikroserwisy oraz separacja środowisk uruchomieniowych.
3. **Automatyzacja i CI/CD:** Podejście Infrastructure as Code (OpenTofu / Terraform), automatyzacja konfiguracji z wykorzystaniem Ansible, potoki testowania i walidacji kodu.
4. **Prywatna infrastruktura i self-hosting:** Prywatne chmury danych (Nextcloud), systemy backupu przyrostowego (BorgBackup, Restic), bezpieczne sieci nakładkowe VPN (WireGuard, Tailscale).
5. **Wdrożenia modeli sztucznej inteligencji:** Uruchamianie i optymalizacja modeli wielkich językowych (Ollama, vLLM, llama.cpp), techniki Retrieval-Augmented Generation (RAG) oraz zarządzanie alokacją akceleratorów obliczeniowych.
6. **Cyberbezpieczeństwo i audyty systemowe:** Hardening systemów Linux, audyty podatności, segmentacja sieciowa, ochrona brzegu sieci (WAF, Reverse Proxy) oraz testy odpornościowe.

---

## Repozytoria Organizacji

Ekosystem koła podzielony jest na dedykowane repozytoria zadaniowe:

| Repozytorium | Widoczność | Opis merytoryczny |
| :--- | :---: | :--- |
| **[`strona-kola`](https://github.com/wskz-devops-lab/strona-kola)** | Publiczne | Oficjalny portal internetowy koła naukowego (GitHub Pages). |
| **[`materialy-dydaktyczne`](https://github.com/wskz-devops-lab/materialy-dydaktyczne)** | Publiczne | Dokumentacja techniczna w modelu Docs-as-Code (MkDocs) — instrukcje wdrożeniowe i katalog 16 projektów laboratoryjnych. |
| **[`architektura-proxmox`](https://github.com/wskz-devops-lab/architektura-proxmox)** | Publiczne | Uniwersalna architektura wirtualizacji, klastrów i laboratoriów na Proxmox VE (Track A): KVM, LXC (nesting), ZFS/Ceph, SDN, GPU Passthrough, IaC. |
| **[`architektura-vdi-opennebula`](https://github.com/wskz-devops-lab/architektura-vdi-opennebula)** | Publiczne | Suwerenna architektura chmurowa VDI na OpenNebula i AlmaLinux 9 (Track B): klonowanie CoW, orkiestracja Ansible/Terraform, portal laboratoryjny. |
| **[`pakiet-red-teaming`](https://github.com/wskz-devops-lab/pakiet-red-teaming)** | Publiczne | Narzędzie automatyzacji audytu bezpieczeństwa, weryfikujące izolację wirtualizacji w 5 kluczowych obszarach ochrony. |
| **[`klaster-gpu-ai`](https://github.com/wskz-devops-lab/klaster-gpu-ai)** | Publiczne | Rozproszony klaster GPU AI i brama Campus AI Gateway (Ollama, LiteLLM, Open WebUI) [W rozwoju]. |

---

## Organizacja i Komunikacja

* 📖 **Przewodnik dla studentów:** [Instrukcja: jak korzystać z GitHuba, brać zadania i zgłaszać PR](https://github.com/wskz-devops-lab/.github/blob/main/INSTRUKCJA_DLA_STUDENTOW.md)
* **Zulip:** Podstawowa platforma wymiany informacji technicznych oraz wideokonferencji (wątek `spotkania online`).
  - Link z zaproszeniem dla członków koła: [Dołącz do przestrzeni Zulip](https://zullip.zarnecki.org/join/yzyh6hrc6i5vro5clnl3uzyb/)
* **Spotkania laboratoryjne:** Zdalne warsztaty praktyczne oraz demonstracje środowisk realizowane w cyklu dwutygodniowym bezpośrednio w Zulipie (zapasowo: Nextcloud Talk).
* **Konsultacje projektowe:** Dyżury merytoryczne i przeglądy postępów prac zespołowych (rezerwacja w kalendarzu chmury).

---

<div align="center">
<sub>Koło Naukowe DevOps & Virtualization Lab · Wyższa Szkoła Kształcenia Zawodowego</sub>
</div>
