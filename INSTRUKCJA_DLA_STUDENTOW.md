# 🎓 Przewodnik Członka Koła Naukowego — DevOps & Virtualization Lab (WSKZ)

Cześć! Witaj w **DevOps & Virtualization Lab** przy Wyższej Szkole Kształcenia Zawodowego.  
Ten przewodnik wyjaśnia krok po kroku, jak korzystamy z GitHuba, jak brać udział w projektach oraz jak oddawać swoje zadania.

---

## 🧭 Krok 1: Twoje konto i narzędzia

### 1. Komunikacja i spotkania (Zulip)
Naszym głównym centrum dowodzenia, dyskusji technicznych i spotkań wideo jest **Zulip**.  
* **Dostęp do platformy:** Imienne zaproszenie do przestrzeni Zulip otrzymasz bezpośrednio od opiekuna koła na Twój adres e-mail podany przy zapisie.
* Po dołączeniu przywitaj się na kanale ogólnym i napisz, jakie obszary Cię interesują (Proxmox, wirtualizacja, kontenery, cyberbezpieczeństwo, Docs-as-Code czy web-dev).
* **Spotkania online:** Warsztaty i spotkania koła odbywają się bezpośrednio w Zulipie – w dedykowanym wątku **`spotkania online`** (uruchamiane przez wbudowaną integrację wideo). Awaryjnie rezerwowany jest pokój w Nextcloud Talk.

### 2. GitHub i Zespół Studenci
* Otrzymasz e-mail z zaproszeniem do organizacji **`wskz-devops-lab`**.
* Po zaakceptowaniu zaproszenia stajesz się członkiem zespołu **`@wskz-devops-lab/studenci`**.
* Dzięki temu masz dostęp do prywatnych i publicznych repozytoriów koła.
* **Ważne:** Skonfiguruj klucz SSH na swoim koncie GitHub ([Oficjalny poradnik GitHuba](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)).

---

## 🎯 Krok 2: Gdzie szukać zadań i jak wybrać projekt?

1. Przejdź do formularza zgłoszeniowego: 👉 [**Wybierz lub zgłoś projekt w Issues**](https://github.com/wskz-devops-lab/.github/issues/new?template=05_zgloszenie_projektu.yml).
2. Szukaj zadań i zgłoszeń z etykietami:
   * `good first issue` – idealne, proste zadania na start (np. poprawka w dokumentacji, prosty skrypt).
   * `🟢 Początkujący` – nie wymagają zaawansowanej wiedzy.
3. Gdy wybierzesz zadanie:
   * Zostaw krótki komentarz w zgłoszeniu (np. *„Chętnie się tym zajmę!”*).
   * Przypisz się do zadania (Assignee).
   * Jeśli utkniesz – napisz na Zulipie lub w komentarzu do Issue!

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

## 🚀 Krok 4: Własny projekt i repozytorium w organizacji (Inkubator)

W naszym kole każdy student może rozwijać **własny projekt laboratoryjny** – samodzielnie lub w 2–3 osobowym zespole. Masz pełne uprawnienia do tworzenia repozytoriów wewnątrz organizacji `wskz-devops-lab`.

### 1. Wybierz ścieżkę startową lub własny pomysł
Możesz wybrać jeden z sugerowanych projektów wstępnych:
* **S1: Własny Homelab i konteneryzacja (Docker Compose / Podman)** — postawienie i zabezpieczenie zestawu usług (Nextcloud, Vaultwarden, dashboard).
* **S2: Bezpieczny dostęp zdalny do laba (Tailscale / WireGuard + Reverse Proxy)** — tunel do domowych maszyn bez wystawiania portów na świat.
* **S3: Lokalny serwer sztucznej inteligencji (Ollama + Open WebUI / LiteLLM / RAG)** — lokalny model językowy z interfejsem webowym i własną bazą wiedzy.
* **S4: Monitoring i obserwowalność (Prometheus + Grafana + Node Exporter)** — dashboard metryk i stanu hosta/kontenerów.
* **S5: Lab detekcji zagrożeń i cyberbezpieczeństwa (Wazuh / Hardening / AD)** — analiza logów, wykrywanie incydentów i utwardzanie systemów.
* **Własny projekt autorski:** Masz pomysł ze swojej pracy, hobby lub uczelni? Realizuj go w ramach koła!

### 2. Zgłoś projekt w Issues koła
1. Otwórz formularz zgłoszeniowy: 👉 [**Zgłoszenie projektu w Issues**](https://github.com/wskz-devops-lab/.github/issues/new?template=05_zgloszenie_projektu.yml).
2. Wybierz swój projekt z listy i opisz w 2–3 zdaniach, co planujesz zrealizować.

### 3. Utwórz repozytorium w organizacji
1. Przejdź do [github.com/wskz-devops-lab](https://github.com/wskz-devops-lab) i kliknij zielony przycisk **`New repository`**.
2. Jako **Owner** upewnij się, że wybrana jest organizacja `wskz-devops-lab`.
3. Nazwij repozytorium według standardu: `projekt-<tematyka>-<twoj-login>` (np. `projekt-homelab-student1`).
4. Zaznacz dodanie pliku `README.md` oraz widoczność (Private lub Public).
5. Wklej link do nowo utworzonego repozytorium w komentarzu pod swoim zgłoszeniem w Issues.

### 4. Co robić dalej? (Praca nad projektem)
1. **Sklonuj repozytorium:** `git clone git@github.com:wskz-devops-lab/projekt-....git`
2. **Dodaj pliki:** Uzupełnij `README.md` o cel i instrukcję uruchomienia, wrzucaj pliki konfiguracyjne (`compose.yaml`, skrypty, playbooki).
3. **Zadawaj pytania i konsultuj:** Twoje zgłoszenie w Issues to otwarty wątek dyskusyjny – pytaj tam o napotkane problemy, a na spotkaniach będziemy omawiać postępy!

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
