# 🚀 Guía Rápida - Iniciar Chatbot con Gemini

## ⚡ Inicio Rápido (2 comandos)

### **Opción 1: Usar scripts automáticos**

```bash
# Backend
start_backend.bat

# Frontend (en otra terminal)
start_frontend.bat
```

### **Opción 2: Comandos manuales**

```bash
# Terminal 1 - Backend
python manage.py runserver

# Terminal 2 - Frontend
cd frontend
npm run dev
```

Luego abre: **http://localhost:5173/chat**

---

## ✅ Verificar que todo funcione

### **Prueba rápida del chatbot:**

```bash
python test_gemini_chatbot.py
```

Deberías ver:
```
✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE
```

---

## 🔧 Si algo no funciona

### **1. Backend no inicia:**
```bash
# Activar entorno virtual
venv_backend\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Intentar de nuevo
python manage.py runserver
```

### **2. Frontend no inicia:**
```bash
cd frontend

# Instalar dependencias
npm install

# Intentar de nuevo
npm run dev
```

### **3. Chatbot no responde:**

**Verifica la API key:**
```bash
# Ver archivo .env
type .env
```

Debería tener:
```env
GEMINI_API_KEY=AIzaSyDeSGpw8EpEhKum3hNfO3yhOt5IXGl9a9o
```

**Probar manualmente:**
```bash
python test_gemini_chatbot.py
```

---

## 📝 URLs Importantes

- **Frontend:** http://localhost:5173/
- **Chat:** http://localhost:5173/chat
- **Backend API:** http://localhost:8000/api/
- **Admin Django:** http://localhost:8000/admin/

---

## 🎯 Endpoints del Chatbot

### **Enviar mensaje:**
```bash
POST http://localhost:8000/api/chatbot/message/

Body:
{
  "message": "¿Qué lugares recomiendas?"
}

Response:
{
  "session_id": "uuid",
  "message": "¿Qué lugares recomiendas?",
  "response": "Te recomiendo...",
  "timestamp": "2024-12-06T21:00:00Z"
}
```

### **Ver historial (requiere login):**
```bash
GET http://localhost:8000/api/chatbot/history/
```

---

## 💡 Tips

- **Primera vez:** Necesitas crear una cuenta en el frontend
- **Chat:** Solo funciona para usuarios logueados
- **API Key:** Ya está configurada en `.env`
- **Gratis:** Gemini es 100% gratis, sin límites de cuota

---

## 📚 Documentación Completa

- **Configuración:** `CONFIGURACION_GEMINI.md`
- **Migración:** `MIGRACION_GEMINI_COMPLETADA.md`
- **General:** `README.md`

---

## 🆘 Ayuda Rápida

```bash
# Ver logs del backend
python manage.py runserver
# (Errores aparecen en la terminal)

# Ver logs del frontend
npm run dev
# (Errores aparecen en la consola del navegador - F12)

# Probar chatbot sin frontend
python test_gemini_chatbot.py
```

---

## ✅ Sistema Listo

Si ves esto en la terminal del backend:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Y esto en el frontend:
```
➜  Local:   http://localhost:5173/
```

**¡Todo está funcionando! 🎉**

Ve a http://localhost:5173/chat y comienza a conversar con el bot.
