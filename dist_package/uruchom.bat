@echo off
:: ============================================================
:: CisiCode - Launcher
:: Kliknij dwukrotnie, żeby uruchomić CisiCode.
:: ============================================================
setlocal

:: Laduj konfiguracje z pliku domyslnego uzytkownika
if exist "%USERPROFILE%\.cisicode.env" (
    for /f "usebackq tokens=1,* delims==" %%A in ("%USERPROFILE%\.cisicode.env") do (
        if not "%%A"=="" if not "%%A:~0,1%"=="#" (
            set "%%A=%%B"
        )
    )
)

echo ============================================================
echo  CisiCode - AI asystent programowania
echo  Zamknij to okno lub wpisz /exit, zeby zakonczyc.
echo ============================================================
echo.

cisicode %*

if errorlevel 1 (
    echo.
    echo [BLAD] CisiCode zakonczyl sie z bledem.
    echo Upewnij sie ze plik %USERPROFILE%\.cisicode.env jest poprawnie skonfigurowany.
    pause
)
