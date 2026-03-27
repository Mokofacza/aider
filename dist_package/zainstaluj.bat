@echo off
:: ============================================================
:: CisiCode - Instalator
:: Uruchom ten plik RAZ, żeby zainstalować CisiCode.
:: Wymaga zainstalowanego Pythona 3.10-3.12.
:: ============================================================
setlocal

echo ============================================================
echo  Instalator CisiCode
echo ============================================================
echo.

:: Sprawdz czy Python jest dostepny
python --version >nul 2>&1
if errorlevel 1 (
    echo [BLAD] Python nie jest zainstalowany lub nie jest w PATH.
    echo.
    echo Pobierz Python 3.11 z: https://www.python.org/downloads/
    echo WAZNE: podczas instalacji zaznacz "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo [OK] Python znaleziony.
echo.

:: Znajdz plik whl w tym samym folderze
for %%f in ("%~dp0cisicode*.whl") do set WHL=%%f

if not defined WHL (
    echo [BLAD] Nie znaleziono pliku cisicode*.whl w folderze:
    echo %~dp0
    pause
    exit /b 1
)

echo Instalowanie: %WHL%
echo.
pip install "%WHL%" --force-reinstall --quiet
if errorlevel 1 (
    echo [BLAD] Instalacja nie powiodla sie.
    pause
    exit /b 1
)

echo.
echo [OK] CisiCode zainstalowany!
echo.

:: Skonfiguruj .env jesli go nie ma
if not exist "%USERPROFILE%\.cisicode.env" (
    if exist "%~dp0.env.example" (
        copy "%~dp0.env.example" "%USERPROFILE%\.cisicode.env" >nul
        echo Stworzono plik konfiguracji: %USERPROFILE%\.cisicode.env
        echo.
        echo !! WAZNE: Edytuj ten plik i wpisz swoj klucz API !!
        echo    Otwiera sie teraz w Notatniku...
        echo.
        notepad "%USERPROFILE%\.cisicode.env"
    )
)

echo.
echo Gotowe! Mozesz teraz uruchamiac CisiCode przez 'uruchom.bat'
echo lub wpisujac 'cisicode' w terminalu.
echo.
pause
