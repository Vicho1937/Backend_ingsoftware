@echo off
echo ========================================
echo Iniciando Frontend - Ruta Local
echo ========================================
echo.

cd /d "%~dp0\frontend"

echo Verificando instalacion de dependencias...
if not exist "node_modules" (
    echo Instalando dependencias...
    call npm install
)

echo.
echo Iniciando servidor de desarrollo en http://localhost:5173
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

call npx vite
