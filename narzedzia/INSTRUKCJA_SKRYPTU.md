# Instrukcja Skryptu Synchronizacji Repozytoriów (synchronizuj_github.sh)

Dokument opisuje cel, architekturę działania oraz sposób użycia skryptu powłoki bash `synchronizuj_github.sh`, służącego do automatyzacji zarządzania repozytoriami Koła Naukowego WSKZ w ramach platformy GitHub.

---

## 1. Cel i Wymiar Edukacyjny

W metodyce DevOps jedną z fundamentalnych reguł jest automatyzacja powtarzalnych czynności administracyjnych. Zamiast manualnej konfiguracji wielu repozytoriów za pośrednictwem interfejsu przeglądarki (tzw. ClickOps), zastosowano skrypt powłoki bash integrujący się bezpośrednio z oficjalnym interfejsem wiersza poleceń GitHub CLI (`gh`).

Skrypt eliminuje ryzyko błędów ludzkich, przyspiesza wdrożenie oraz stanowi praktyczny przykład automatyzacji dla studentów koła naukowego.

---

## 2. Bezpieczeństwo i Przetwarzanie Danych

Skrypt **nie zawiera żadnych poufnych danych**:
- Nie przechowuje tokenów API, haseł ani prywatnych kluczy SSH.
- Uwierzytelnianie opiera się na lokalnej sesji użytkownika w narzędziu `gh` (bezpieczny magazyn poświadczeń systemu operacyjnego / keyring) oraz protokole SSH (`git@github.com`).
- Może być w pełni publicznie udostępniany członkom koła i osobom przeglądającym repozytorium.

---

## 3. Zasada Działania Skryptu

Procedura wykonywana przez skrypt przebiega w następujących krokach:

1. **Weryfikacja autoryzacji:**
   Sprawdzenie statusu sesji za pomocą polecenia `gh auth status`. W przypadku braku aktywnej sesji skrypt informuje użytkownika o konieczności logowania komendą `gh auth login -w -p ssh`.
2. **Identyfikacja organizacji:**
   Pobranie nazwy docelowej organizacji przekazanej jako argument wywołania lub zapytanie interaktywne.
3. **Pętla przetwarzania repozytoriów:**
   Dla każdego z zdefiniowanych katalogów roboczych:
   - Weryfikacja, czy repozytorium istnieje już w organizacji (`gh repo view`).
   - Jeśli nie istnieje – utworzenie nowego repozytorium zdalnego poleceniem `gh repo create` wraz z określeniem widoczności (publiczne/prywatne) oraz opisu.
   - Konfiguracja adresu zdalnego `origin` w formacie SSH (`git@github.com:<organizacja>/<repozytorium>.git`).
   - Wypchnięcie gałęzi `main` na serwer zdalny poleceniem `git push -u origin main`.

---

## 4. Wymagania Wstępne i Uruchomienie

### Wymagania:
- System operacyjny z rodziny Linux / macOS.
- Zainstalowane narzędzie Git oraz GitHub CLI (`gh` w wersji 2.100+).
- Skonfigurowany i dodany do profilu GitHub klucz SSH.

### Sposób użycia:

```bash
# Nadanie uprawnień do wykonania (jeśli wymagane)
chmod +x synchronizuj_github.sh

# Uruchomienie z podaniem nazwy organizacji
./synchronizuj_github.sh wskz-devops-lab
```
