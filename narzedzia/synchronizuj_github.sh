#!/usr/bin/env bash
# ==============================================================================
# Skrypt synchronizacji repozytoriów Koła Naukowego WSKZ z organizacją na GitHubie
# ==============================================================================

set -euo pipefail

ORG_NAME=${1:-""}

echo -e "\033[1;34m====================================================================\033[0m"
echo -e "\033[1;32m  Koło Naukowe DevOps & Virtualization Lab (WSKZ) - GitHub Sync     \033[0m"
echo -e "\033[1;34m====================================================================\033[0m"

# 1. Sprawdzenie autoryzacji w gh CLI
if ! gh auth status >/dev/null 2>&1; then
    echo -e "\n\033[1;33m[UWAGA]\033[0m Nie jesteś jeszcze zalogowany w GitHub CLI ('gh')."
    echo -e "Aby się zalogować, uruchom w terminalu:"
    echo -e "    \033[1;36mgh auth login -w -p ssh\033[0m"
    echo -e "Po zalogowaniu uruchom ten skrypt ponownie:\n"
    exit 1
fi

# 2. Pobranie nazwy organizacji
if [ -z "$ORG_NAME" ]; then
    echo -e "\nDostępne organizacje dla Twojego konta:"
    gh org list || true
    echo ""
    read -rp "Podaj nazwę organizacji na GitHubie (np. wskz-devops-lab): " ORG_NAME
fi

if [ -z "$ORG_NAME" ]; then
    echo -e "\033[1;31mBłąd:\033[0m Nie podano nazwy organizacji."
    exit 1
fi

echo -e "\nDocelowa organizacja: \033[1;36mhttps://github.com/$ORG_NAME\033[0m\n"

# 3. Definicja repozytoriów: (katalog lokalny | nazwa na GH | widoczność | opis)
REPOS=(
    "repozytoria/01_profil_organizacji|.github|public|Profil i strona główna organizacji Koła Naukowego WSKZ"
    "repozytoria/02_materialy_dydaktyczne|materialy-dydaktyczne|public|Baza wiedzy Docs-as-Code (MkDocs) - projekty 1-16 i poradniki"
    "repozytoria/03_strona_kola|strona-kola|public|Publiczny portal WWW koła naukowego (GitHub Pages)"
    "repozytoria/04_architektura_vdi|architektura-vdi-proxmox|public|Praktyczna architektura wirtualnych laboratoriów VDI na Proxmox VE (Golden Image, noVNC, Terraform)"
    "repozytoria/05_pakiet_red_teaming|pakiet-red-teaming|public|Zautomatyzowany pakiet audytu bezpieczeństwa i testów Red Teaming (5 filarów ochrony)"
)

for entry in "${REPOS[@]}"; do
    IFS="|" read -r LOCAL_DIR REMOTE_NAME VISIBILITY DESCRIPTION <<< "$entry"

    echo -e "\033[1;34m--------------------------------------------------------------------\033[0m"
    echo -e "\033[1;32m--> Przetwarzanie: $REMOTE_NAME ($VISIBILITY)\033[0m"
    echo -e "    Katalog: $LOCAL_DIR"

    (
        cd "$LOCAL_DIR"

        # Tworzenie repozytorium zdalnego, jeśli nie istnieje
        if ! gh repo view "$ORG_NAME/$REMOTE_NAME" >/dev/null 2>&1; then
            echo "    Tworzenie zdalnego repozytorium na GitHubie..."
            gh repo create "$ORG_NAME/$REMOTE_NAME" \
                --"$VISIBILITY" \
                --description "$DESCRIPTION" \
                || true
        else
            echo "    Zdalne repozytorium już istnieje na GitHubie."
        fi

        # Konfiguracja remote origin (SSH)
        REMOTE_URL="git@github.com:${ORG_NAME}/${REMOTE_NAME}.git"
        if git remote | grep -q "^origin$"; then
            git remote set-url origin "$REMOTE_URL"
        else
            git remote add origin "$REMOTE_URL"
        fi

        echo "    Wypychanie zmian do gałęzi main..."
        git branch -M main
        git push -u origin main || echo -e "    \033[1;33m[INFO]\033[0m Upewnij się, że masz uprawnienia do organizacji."
    )
done

echo -e "\n\033[1;32m====================================================================\033[0m"
echo -e "\033[1;32m  SYNCHRONIZACJA ZAKOŃCZONA SUKCESEM!                              \033[0m"
echo -e "\033[1;32m  Zobacz swoją organizację: https://github.com/$ORG_NAME            \033[0m"
echo -e "\033[1;32m====================================================================\033[0m"
