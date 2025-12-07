# 🚀 DESPLEGAR FRONTEND EN VERCEL

## 📝 **PREREQUISITO:**

✅ Backend desplegado en Railway
✅ URL del backend: `https://tu-backend.railway.app`

---

## 🔧 **PASO 1: CONFIGURAR FRONTEND**

### **A) Actualizar API URL:**

Edita: `frontend/src/services/api.js`

```javascript
import axios from 'axios'

const api = axios.create({
  // En producción, usa la URL de Railway
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
})

// ... resto del código
```

### **B) Crear archivo de configuración:**

Crea: `frontend/.env.production`

```env
VITE_API_URL=https://tu-backend.railway.app
```

### **C) Subir cambios a GitHub:**

1. Abre GitHub Desktop
2. Commit: "Configure production API URL"
3. Push origin

---

## 🌐 **PASO 2: DESPLEGAR EN VERCEL**

### **A) Crear cuenta:**
1. Ve a: https://vercel.com/
2. Click en **"Sign Up"**
3. Selecciona **"Continue with GitHub"**
4. Autoriza Vercel

### **B) Importar Proyecto:**
1. En Vercel, click en **"Add New..."** → **"Project"**
2. Busca: **Vicho1937/Backend_ingsoftware**
3. Click en **"Import"**

### **C) Configurar Build:**

**Root Directory:**
```
frontend
```

**Framework Preset:**
```
Vite
```

**Build Command:**
```
npm run build
```

**Output Directory:**
```
dist
```

### **D) Variables de Entorno:**

Click en **"Environment Variables"** y agrega:

```
VITE_API_URL=https://tu-backend.railway.app
```

### **E) Deploy:**
1. Click en **"Deploy"**
2. Espera 1-2 minutos
3. Vercel te dará una URL: `https://tu-proyecto.vercel.app`

---

## 🔄 **PASO 3: ACTUALIZAR CORS EN BACKEND**

### **En Railway (Backend):**

1. Ve a tu proyecto en Railway
2. Tab **"Variables"**
3. Edita `CORS_ALLOWED_ORIGINS`:

```
CORS_ALLOWED_ORIGINS=https://tu-proyecto.vercel.app,https://tu-proyecto-git-main.vercel.app
```

4. Railway se reiniciará automáticamente

---

## ✅ **PASO 4: VERIFICAR QUE TODO FUNCIONE**

Abre tu frontend en Vercel:
```
https://tu-proyecto.vercel.app
```

Verifica:
- ✅ La página carga
- ✅ Los lugares se muestran
- ✅ Puedes registrarte/login
- ✅ El chatbot responde
- ✅ Los favoritos funcionan

---

## ⚠️ **PROBLEMAS COMUNES:**

### **Error: "Network Error"**
- Verifica que `VITE_API_URL` esté correcta
- Verifica que CORS esté configurado en Railway

### **Error: "CORS policy"**
- Agrega la URL de Vercel a `CORS_ALLOWED_ORIGINS` en Railway
- Incluye TODAS las variantes de URL de Vercel

### **Frontend carga pero sin datos:**
- Verifica que el backend esté funcionando: `https://tu-backend.railway.app/api/routes/`
- Revisa la consola del navegador (F12)

---

## 🎯 **URLs FINALES:**

✅ **Backend (Railway):**
```
https://__________.railway.app
```

✅ **Frontend (Vercel):**
```
https://__________.vercel.app
```

---

## 📝 **NOTAS:**

1. **Vercel es GRATIS** para proyectos personales
2. **Auto-deploy:** Cada push a GitHub actualiza Vercel automáticamente
3. **Dominio custom:** Puedes agregar tu propio dominio en Vercel
4. **Preview URLs:** Vercel crea URLs de preview para cada branch

---

¡Proyecto 100% desplegado! 🎉
