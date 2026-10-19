# 🎓 Przewodnik Członka Koła Naukowego — DevOps & Virtualization Lab (WSKZ)

Cześć! Witaj w **DevOps & Virtualization Lab** przy Wyższej Szkole Kształcenia Zawodowego.  
Ten przewodnik wyjaśnia krok po kroku, jak korzystamy z GitHuba, jak brać udział w projektach oraz jak oddawać swoje zadania.

---

## 🧭 Krok 1: Twoje konto i narzędzia

### 1. Komunikacja (Zulip)
Naszym głównym centrum dowodzenia i dyskusji technicznych jest **Zulip**.  
👉 **Dołącz tutaj:** [Zaproszenie do przestrzeni Zulip Koła](https://zullip.zarnecki.org/join/yzyh6hrc6i5vro5clnl3uzyb/)
* Po dołączeniu przywitaj się na kanale ogólnym i napisz, jakie obszary Cię interesują (Proxmox, wirtualizacja, kontenery, cyberbezpieczeństwo, Docs-as-Code czy web-dev).

### 2. GitHub i Zespół Studenci
* Otrzymasz e-mail z zaproszeniem do organizacji **`wskz-devops-lab`**.
* Po zaakceptowaniu zaproszenia stajesz się członkiem zespołu **`@wskz-devops-lab/studenci`**.
* Dzięki temu masz dostęp do prywatnych i publicznych repozytoriów koła.
* **Ważne:** Skonfiguruj klucz SSH na swoim koncie GitHub ([Oficjalny poradnik GitHuba](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)).

---

## 🎯 Krok 2: Gdzie szukać zadań?

1. Przejdź do zakładki **Projects** w organizacji: [Tablica Projektów Koła](https://github.com/orgs/wskz-devops-lab/projects).
2. Szukaj zadań z etykietami:
   * `good first issue` – idealne, proste zadania na start (np. poprawka w dokumentacji, prosty skrypt).
   * `🟢 Początkujący` – nie wymagają zaawansowanej wiedzy.
3. Gdy wybierzesz zadanie:
   * Zostaw krótki komentarz w zgłoszeniu (np. *„Chętnie się tym zajmę!”*).
   * Przypisz się do zadania (Assignee) i przesuń kartę do kolumny **W trakcie (In Progress)**.
   * Jeśli utkniesz – napisz na Zulipie w wątku projektu!

---

## 💻 Krok 3: Jak pracować z kodem (Git Workflow)

W kole uczymy się rynkowych standardów pracy zespołowej. **Nigdy nie pracujemy bezpośrednio na gałęzi `main`.**

### 1. Pobierz repozytorium na swój komputer
```bash
git clone git@github.com:wskz-devops-lab/NAZWA_REPOZYTORIUM.git
cd NAZWA_REPOZYTORIUM
```

### 2. Utwórz nową gałąź (branch) dla swojego zadania
Nazwa gałęzi powinna mówić, co robisz:
```bash
# Dla nowej funkcji lub instrukcji:
git checkout -b feat/instrukcja-wireguard-proxmox

# Dla poprawki błędu:
git checkout -b fix/literowka-w-projekcie-03
```

### 3. Wprowadź zmiany i przetestuj je
Pracuj lokalnie lub na testowej maszynie wirtualnej:
* Jeśli piszesz dokumentację: sprawdź podgląd w MkDocs (`mkdocs serve`).
* Jeśli piszesz skrypt: przetestuj go na czystym kontenerze/maszynie.

### 4. ⚠️ KRYTYCZNE: Bezpieczeństwo i Higiena Kodu
Przed zrobieniem commita ZAWSZE upewnij się:
* **ŻADNYCH HASEŁ ANI KLUCZY PRYWATNYCH:** Nie commituj plików `.env` z sekretami, kluczy SSH `id_rsa`, ani haseł roota.
* Wszelkie wrażliwe dane zastąp placeholderami (np. `YOUR_PASSWORD_HERE` lub zmienną `$VAULT_SECRET`).

### 5. Zapisz zmiany i wyślij gałąź na GitHuba
```bash
git add .
git commit -m "feat(docs): dodano instrukcję konfiguracji WireGuarda w kontenerze LXC"
git push -u origin feat/instrukcja-wireguard-proxmox
```

---

## 🔍 Krok 4: Oddanie zadania (Pull Request i Code Review)

1. Po wysłaniu gałęzi wejdź na GitHuba do danego repozytorium.
2. Zobaczysz żółty pasek z przyciskiem **`Compare & pull request`** – kliknij go.
3. W opisie PR-a zobaczysz **szablon z checklistą**:
   * Zaznacz ptaszkami `[x]` wykonane punkty (brak sekretów, przetestowanie kodu).
   * Napisz krótko, co zostało zrobione.
   * Jeśli zadanie ma swój numer w Issues, dopisz np. `Closes #12`.
4. Kliknij **`Create pull request`**.
5. Daj znać na Zulipie w kanale projektu:
   > *„Hej, otworzyłem PR #15 z instrukcją WireGuarda. Proszę o review!”*
6. **Code Review:** Mentor lub inny członek koła przejrzy Twój kod, może zostawić komentarze lub sugestie. To nie egzamin – to okazja do nauki!
7. Po zaakceptowaniu zmian (Approve), kod zostaje włączony do gałęzi `main`. Twoja praca jest częścią projektu! 🎉

---

## 💡 Jak zgłaszać nowe pomysły lub błędy?

Jeśli masz pomysł na nowe laboratorium, skrypt automatyzacji lub zauważyłeś błąd:
1. Wejdź w zakładkę **Issues** danego repozytorium.
2. Kliknij **`New issue`**.
3. Wybierz odpowiedni kafelek:
   * 📚 **Nowe ćwiczenie / Poradnik laboratoryjny**
   * ⚙️ **Moduł Infrastruktury / Automatyzacja IaC**
   * 🛡️ **Nowy test audytu bezpieczeństwa**
   * 🐛 **Błąd w konfiguracji / środowisku lab**
4. Wypełnij prosty formularz i zatwierdź.

---

## 🤝 Złote Zasady Koła
1. **Nie bój się pytać:** Każdy z nas kiedyś zaczynał. Zulip jest po to, aby zadawać pytania.
2. **Ucz się przez praktykę:** Lepiej zrobić mały krok i zepsuć maszynę wirtualną w labie (i postawić ją na nowo!), niż tylko czytać teorię.
3. **Buduj swoje portfolio:** Każdy zaakceptowany Pull Request to zielony kwadracik na Twoim profilu GitHub i realne doświadczenie, które wpiszesz do CV.
