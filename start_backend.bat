@echo off
echo ========================================
echo Iniciando Backend - Ruta Local
echo ========================================
echo.

cd /d "%~dp0"

echo Activando entorno virtual...
call venv_backend\Scripts\activate.bat

echo.
echo Aplicando migraciones...
python manage.py migrate

echo.
echo Iniciando servidor Django en http://localhost:8000
echo Panel Admin: http://localhost:8000/admin
echo API: http://localhost:8000/api/
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

python manage.py runserver
