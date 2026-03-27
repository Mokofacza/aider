# CisiCode - pakiet instalacyjny

Ten folder zawiera wszystko, co jest potrzebne do uruchomienia CisiCode na dowolnym komputerze z systemem Windows i zainstalowanym językiem Python.

## Wymagania

- System Windows
- Zainstalowany **Python w wersji 3.10-3.12** (najlepiej 3.11).
  - Pobierz z: `https://www.python.org/downloads/`
  - **WAŻNE:** Podczas instalacji Pythona koniecznie zaznacz opcję **"Add Python to PATH"** (Dodaj Python do zmiennych środowiskowych).

## Instalacja krok po kroku

1. Skopiuj ten cały folder (`dist_package`) w docelowe miejsce na dysku (np. `C:\Programy\Cisicode`).
2. Kliknij dwukrotnie plik **`zainstaluj.bat`**.
   - Skrypt sprawdzi, czy masz zainstalowanego Pythona.
   - Zainstaluje CisiCode (może to potrwać dłuższą chwilę przy pierwszym uruchomieniu, instalują się zależności).
   - Na sam koniec **otworzy się Notatnik** z plikiem konfiguracyjnym `.cisicode.env`.
3. **W Notatniku uzupełnij konfigurację:**
   - Podaj właściwy `OPENAI_API_BASE` (adres serwera).
   - Wklej swój `OPENAI_API_KEY`.
   - Zapisz plik (Ctrl+S) i zamknij Notatnik.

## Codzienne używanie

Aby uruchomić aplikację:
- Otwórz folder i kliknij dwukrotnie **`uruchom.bat`**.

*Alternatywnie:* (jeśli Python jest w PATH) możesz otworzyć dowolny terminal (CMD, PowerShell) w folderze swojego projektu i po prostu wpisać:
```bash
cisicode
```
lub
```bash
cisicode --model azure/o4-mini
```

## Zmiana konfiguracji w przyszłości

Twój plik z kluczami API znajduje się w Twoim folderze domowym:\
`C:\Users\TWOJA_NAZWA\.cisicode.env` (lub wejdź w `%USERPROFILE%\.cisicode.env` z paska adresu).

Ogólna konfiguracja CisiCode jest w pliku `.aider.conf.yml` w tym folderze. Skopiuj go do głównego katalogu swojego projektu by zmienić domyślny język czy inne ustawienia specjalnie dla danego projektu.
