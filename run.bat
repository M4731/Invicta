@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo Lipseste mediul virtual. Ruleaza mai intai setup.bat.
    pause
    exit /b 1
)
if not exist "invicta\.env" (
    echo Lipseste invicta\.env. Ruleaza mai intai setup.bat.
    pause
    exit /b 1
)
echo Deschide http://127.0.0.1:8000/ in browser dupa pornirea serverului.
echo Pastreaza aceasta fereastra deschisa. Pentru oprire, apasa Ctrl+C.
".venv\Scripts\python.exe" "invicta\manage.py" runserver 127.0.0.1:8000
set "result=%errorlevel%"
echo.
pause
exit /b %result%
