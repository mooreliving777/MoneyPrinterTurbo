@echo off
setlocal
cd /d "%~dp0"

echo ============================================================
echo   MOORE MEDIA AI - AI Production Studio
echo ============================================================

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" moore_media_ai_launcher.py
    goto :end
)

where uv >nul 2>nul
if not errorlevel 1 (
    uv run python moore_media_ai_launcher.py
    goto :end
)

echo.
echo Moore Media AI could not find the project Python environment.
echo Run these commands first from this folder:
echo.
echo   uv python install 3.11
echo   uv sync --frozen
echo.
pause

:end
endlocal
