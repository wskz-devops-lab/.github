## 📝 Opis zmian
Krótki opis: co zmienia ten PR i którego projektu dotyczy?
Powiązane zgłoszenie: Closes #

## 🎯 Komponent / Środowisko
- [ ] Proxmox VE / KVM / LXC
- [ ] OpenNebula / VDI
- [ ] Automatyzacja (Ansible / OpenTofu / Bash)
- [ ] Baza wiedzy (MkDocs / Materiały dydaktyczne)
- [ ] Pakiet audytu / Red Teaming
- [ ] Strona koła (React / Vite)

## 🧪 Jak zmiany zostały przetestowane?
*Opisz, jak sprawdziłeś kod (np. odpalenie playbooka z `--check`, uruchomienie w maszynie testowej LXC/VM, `mkdocs serve`, `npm run build`):*

## 🔒 Bezpieczeństwo i Higiena Kodu (KRYTYCZNE)
- [ ] **Brak sekretów:** Upewniłem się, że kod NIE zawiera haseł, tokenów API ani prywatnych kluczy SSH (użyto zmiennych środowiskowych lub `vault`)
- [ ] **Składnia:** Skrypty przeszły walidację (`shellcheck` / `ansible-lint` / `terraform fmt` / `eslint`)
- [ ] **Dokumentacja:** Zaktualizowano README lub odpowiedni plik w `materialy-dydaktyczne`
- [ ] **Zgłoszenie:** Poinformowałem o PR na Zulipie w odpowiednim kanale
