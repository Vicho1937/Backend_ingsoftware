@echo off
echo ========================================
echo Setup Inicial - Ruta Local
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Activando entorno virtual...
call venv_backend\Scripts\activate.bat

echo.
echo [2/5] Instalando dependencias de Python...
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-filter python-dotenv openai

echo.
echo [3/5] Aplicando migraciones de base de datos...
python manage.py makemigrations
python manage.py migrate

echo.
echo [4/5] Creando superusuario...
echo Ingresa los datos del administrador:
python manage.py createsuperuser

echo.
echo [5/5] Instalando dependencias del frontend...
cd frontend
call npm install

echo.
echo ========================================
echo Setup completado!
echo ========================================
echo.
echo Proximos pasos:
echo 1. Ejecuta start_backend.bat para iniciar el backend
echo 2. Ejecuta start_frontend.bat para iniciar el frontend
echo 3. Accede a http://localhost:5173
echo.
echo Panel Admin: http://localhost:8000/admin
echo.
pause
