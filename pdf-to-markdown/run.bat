@echo off
REM Spustí PDF -> Markdown aplikaci a otevře ji v prohlížeči.
cd /d "%~dp0"

REM Při prvním spuštění doinstaluje závislosti (jen pokud chybí markitdown).
py -c "import markitdown, flask" 2>nul
if errorlevel 1 (
    echo Instaluji zavislosti, chvili to potrva...
    py -m pip install -r requirements.txt
)

REM Otevre se jako samostatne okno aplikace.
py app.py
pause
