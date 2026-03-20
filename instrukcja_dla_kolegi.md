# Jak zainstalować i używać Cisicode (wersja dla kolegi)

Dzięki temu plikowi będziesz mógł używać `cisicode` z dowolnego miejsca w systemie, bez konieczności kopiowania pliku `.exe` do każdego folderu.

## Co otrzymałeś:
1.  `cisicode.exe` - główny program.
2.  `dodaj_do_path.ps1` - skrypt instalacyjny (opcjonalny).

## Instrukcja instalacji (Raz na zawsze)

1.  **Wybierz stałe miejsce:** Umieść pliki `cisicode.exe` i `dodaj_do_path.ps1` w folderze, z którego ich **nie usuniesz**.
    *   *Przykład:* Stwórz folder `C:\Tools` lub `C:\Programy\Cisicode` i tam wklej oba pliki.
2.  **Uruchom skrypt instalacyjny:**
    *   Kliknij prawym przyciskiem myszy na plik `dodaj_do_path.ps1`.
    *   Wybierz **"Uruchom za pomocą programu PowerShell"** (Run with PowerShell).
    *   Skrypt doda ten folder do systemowej zmiennej PATH.
3.  **Zrestartuj terminal:** Zamknij wszystkie otwarte okna terminala (CMD, PowerShell, VS Code) i otwórz je ponownie.

## Jak używać?

Teraz możesz otworzyć terminal w **dowolnym folderze** (np. w swoim projekcie) i wpisać po prostu:

```bash
cisicode --model azure/o4-mini
```

Program uruchomi się, nawet jeśli plik `.exe` jest w innym miejscu.

---
**Ważne:** Pamiętaj o ustawieniu zmiennych środowiskowych dla Azure (np. `AZURE_API_KEY`, `AZURE_API_BASE`), aby program mógł połączyć się z modelem AI.
