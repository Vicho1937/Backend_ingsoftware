# 📦 SUBIR PROYECTO A GITHUB

## ✅ **PASO 1: Instalar Git**

1. Descarga Git desde: https://git-scm.com/download/win
2. Instala con las opciones por defecto
3. Reinicia la terminal

## ✅ **PASO 2: Verificar que .env esté protegido**

El archivo `.gitignore` ya está configurado para ignorar:
- `.env` (tus credenciales)
- `venv_backend/` (entorno virtual)
- `node_modules/` (dependencias frontend)
- `db.sqlite3` (base de datos local)
- `__pycache__/` (archivos temporales)

**✅ Tu archivo `.env.example` es seguro y puede subirse**

## ✅ **PASO 3: Crear Repositorio en GitHub**

1. Ve a: https://github.com/new
2. Nombre del repositorio: `ruta-local-santiago` (o el que quieras)
3. Descripción: "Plataforma web para descubrir lugares locales en Santiago"
4. **NO** marques "Add a README file"
5. **NO** marques "Add .gitignore"
6. Click en "Create repository"

## ✅ **PASO 4: Subir el código**

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
# Inicializar repositorio Git
git init

# Agregar todos los archivos (excepto los del .gitignore)
git add .

# Verificar qué archivos se van a subir (IMPORTANTE)
git status

# Crear primer commit
git commit -m "Initial commit: Proyecto Ruta Local completo"

# Conectar con GitHub (reemplaza TU_USUARIO y TU_REPO)
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git

# Subir el código
git push -u origin main
```

## ✅ **PASO 5: Verificar que .env NO se subió**

1. Ve a tu repositorio en GitHub
2. Verifica que **NO** aparezca el archivo `.env`
3. Verifica que **SÍ** aparezca `.env.example`
4. Verifica que **NO** aparezca `venv_backend/`

## 🚨 **SI .env SE SUBIÓ POR ERROR**

```powershell
# Eliminar .env del repositorio (sin borrarlo localmente)
git rm --cached .env

# Crear nuevo commit
git commit -m "Remove .env from repository"

# Subir cambios
git push

# IMPORTANTE: Cambiar todas las contraseñas en Supabase
```

## ✅ **PASO 6: Preparar para Railway/Vercel**

Una vez en GitHub, estarás listo para:
- **Backend → Railway**
- **Frontend → Vercel**

---

## 📝 **ARCHIVOS QUE SE SUBIRÁN:**

✅ Código fuente (`.py`, `.jsx`, `.css`)
✅ `requirements.txt`
✅ `.gitignore`
✅ `.env.example`
✅ `README.md`
✅ Documentación (`.md`)

## 🚫 **ARCHIVOS QUE NO SE SUBIRÁN:**

❌ `.env` (credenciales)
❌ `venv_backend/` (entorno virtual)
❌ `node_modules/` (dependencias)
❌ `__pycache__/` (archivos temporales)
❌ `db.sqlite3` (base de datos local)

---

¡Listo para subir! 🚀
