# 🚀 DESPLEGAR BACKEND EN RAILWAY

## ✅ **ARCHIVOS PREPARADOS:**

- ✅ `Procfile` - Comando para iniciar Gunicorn
- ✅ `runtime.txt` - Versión de Python (3.11.9)
- ✅ `railway.json` - Configuración de Railway
- ✅ `requirements.txt` - Con gunicorn y whitenoise
- ✅ `settings.py` - WhiteNoise configurado

---

## 📦 **PASO 1: SUBIR CAMBIOS A GITHUB**

Abre GitHub Desktop:
1. Verás los nuevos archivos (Procfile, runtime.txt, railway.json)
2. Escribe el commit: "Add Railway deployment files"
3. Click en **"Commit to main"**
4. Click en **"Push origin"**

---

## 🚂 **PASO 2: CREAR CUENTA EN RAILWAY**

1. Ve a: https://railway.app/
2. Click en **"Login"**
3. Selecciona **"Login with GitHub"**
4. Autoriza Railway para acceder a tus repos

---

## 🚀 **PASO 3: DESPLEGAR BACKEND**

### **A) Crear Proyecto:**
1. En Railway, click en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Busca y selecciona: **Vicho1937/Backend_ingsoftware**
4. Railway detectará automáticamente que es Django

### **B) Configurar Variables de Entorno:**

Click en tu proyecto → Tab **"Variables"** → Agregar las siguientes:

```
DATABASE_URL=postgresql://postgres.aouypionjbonohgyuejj:Vicho1937.@aws-0-us-west-2.pooler.supabase.com:6543/postgres

SECRET_KEY=django-insecure-change-this-in-production

GEMINI_API_KEY=AIzaSyDeSGpw8EpEhKum3hNfO3yhOt5IXGl9a9o

DEBUG=False

ALLOWED_HOSTS=*.railway.app

CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app
```

### **C) Desplegar:**
1. Railway empezará a construir automáticamente
2. Espera 2-3 minutos
3. Una vez desplegado, copia la URL: `https://tu-backend.railway.app`

### **D) Cargar Datos (IMPORTANTE):**

Una vez desplegado, ve a:
- **Tab "Deployments"**
- Click en el deployment activo
- Click en **"View Logs"**

Ejecuta manualmente el script de datos:
```bash
# Opción 1: Desde Railway CLI (recomendado)
railway run python force_reload_all.py

# Opción 2: Crear una ruta en Django Admin
# Y ejecutar force_reload_all.py desde ahí
```

---

## 🌐 **PASO 4: VERIFICAR QUE FUNCIONE**

Abre en el navegador:
```
https://tu-backend.railway.app/api/routes/
https://tu-backend.railway.app/api/categories/
https://tu-backend.railway.app/admin/
```

Si ves JSON o la página de admin, **¡FUNCIONA!** ✅

---

## ⚠️ **PROBLEMAS COMUNES:**

### **Error: "Application failed to start"**
- Verifica que todas las variables de entorno estén configuradas
- Revisa los logs en Railway

### **Error: "Could not connect to database"**
- Verifica que `DATABASE_URL` esté correcta
- Asegúrate que Supabase permita conexiones externas

### **Error: "ALLOWED_HOSTS"**
- Agrega la URL de Railway a `ALLOWED_HOSTS`
- Reinicia el deployment

---

## 📝 **NOTAS IMPORTANTES:**

1. **Railway es GRATIS** con $5 USD de crédito mensual
2. **Supabase sigue siendo tu BD** (Railway solo corre el backend)
3. **Guarda la URL** del backend para configurar el frontend
4. **No expongas las variables de entorno** en el código

---

## 🎯 **SIGUIENTE PASO:**

Una vez el backend esté funcionando en Railway, vamos a desplegar el **Frontend en Vercel**.

🔗 URL del Backend: `https://__________.railway.app`

---

¡Listo para Railway! 🚂
