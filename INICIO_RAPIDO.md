# 🚀 INICIO RÁPIDO - Ruta Local

## ⚡ Ejecución Inmediata

### 1️⃣ Iniciar Backend
```bash
start_backend.bat
```
✅ Backend corriendo en: **http://localhost:8000**

### 2️⃣ Iniciar Frontend (nueva terminal)
```bash
start_frontend.bat
```
✅ Frontend corriendo en: **http://localhost:5173**

---

## 🔑 Credenciales de Acceso

### Usuario Demo (Ya creado)
- **Usuario:** `demo`
- **Contraseña:** `demo1234`

### Panel de Administración
- **URL:** http://localhost:8000/admin
- **Usuario:** *(el superusuario que creaste)*
- **Contraseña:** *(tu contraseña de superusuario)*

---

## 📊 Datos Precargados

El sistema ya tiene datos de ejemplo listos para usar:

✅ **8 Categorías**
- 🍽️ Restaurantes
- 🏛️ Turismo
- 🎭 Entretenimiento
- 🌳 Parques
- 🖼️ Museos
- ☕ Cafeterías
- 🌙 Vida Nocturna
- 🛍️ Compras

✅ **8 Rutas de Santiago, Chile**
- La Chascona (Casa de Neruda)
- Cerro San Cristóbal
- Mercado Central
- Café Colmado
- Parque Bicentenario
- Plaza de Armas
- Boragó (Restaurante)
- Museo de la Memoria

---

## 🎯 Qué Puedes Hacer

### Como Usuario Normal
1. **Registrarte o usar usuario demo**
2. **Explorar rutas** con mapas interactivos
3. **Buscar y filtrar** por categoría
4. **Dejar reseñas** y calificaciones
5. **Guardar favoritos**
6. **Chatear con IA** para recomendaciones
7. **Editar tu perfil**

### Como Administrador
1. **Acceder al panel admin**: http://localhost:8000/admin
2. **Crear/Editar/Eliminar**:
   - Categorías
   - Rutas
   - Usuarios
   - Reseñas
3. **Ver estadísticas** del sistema
4. **Moderar contenido**

---

## 🗺️ URLs Importantes

| Servicio | URL | Descripción |
|----------|-----|-------------|
| **Frontend** | http://localhost:5173 | Aplicación web principal |
| **Backend API** | http://localhost:8000/api/ | API REST |
| **Admin Panel** | http://localhost:8000/admin | Panel de administración |
| **API Docs** | http://localhost:8000/api/ | Endpoints disponibles |

---

## 📝 Flujo de Uso Recomendado

### Primera Vez
1. ✅ Ejecuta `start_backend.bat`
2. ✅ Ejecuta `start_frontend.bat` en otra terminal
3. ✅ Abre http://localhost:5173
4. ✅ Inicia sesión con `demo / demo1234`
5. ✅ Explora las rutas precargadas
6. ✅ Prueba el chatbot
7. ✅ Agrega favoritos
8. ✅ Deja una reseña

### Desarrollo
1. El backend se recarga automáticamente con cambios
2. El frontend usa Hot Module Replacement (HMR)
3. Revisa la consola del navegador para debugging
4. Usa el panel admin para gestionar datos

---

## 🔧 Comandos Útiles

### Backend
```bash
# Activar entorno virtual
.\venv_backend\Scripts\activate

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos de ejemplo
python load_sample_data.py

# Shell de Django
python manage.py shell
```

### Frontend
```bash
cd frontend

# Instalar dependencias
npm install

# Modo desarrollo
npm run dev

# Build para producción
npm run build

# Vista previa del build
npm run preview
```

---

## 🐛 Solución de Problemas

### Backend no inicia
```bash
# Verifica que el entorno virtual esté activado
.\venv_backend\Scripts\activate

# Reinstala dependencias
pip install -r requirements.txt

# Verifica migraciones
python manage.py migrate
```

### Frontend no inicia
```bash
cd frontend

# Limpia e instala de nuevo
Remove-Item -Recurse -Force node_modules
npm install
```

### Puerto ocupado
- Backend: Cambia el puerto con `python manage.py runserver 8001`
- Frontend: Cambia en `vite.config.js`

### Chatbot no responde
- Verifica que tengas una API key de OpenAI válida en `.env`
- La key debe tener créditos disponibles

---

## 📞 Endpoints Principales del API

### Autenticación
```
POST /api/auth/register/          # Registrar usuario
POST /api/auth/login/             # Obtener token JWT
POST /api/auth/token/refresh/     # Refrescar token
GET  /api/auth/profile/           # Ver perfil
PUT  /api/auth/profile/           # Actualizar perfil
```

### Rutas
```
GET    /api/routes/               # Listar rutas
GET    /api/routes/:id/           # Detalle de ruta
POST   /api/routes/               # Crear ruta (admin)
POST   /api/routes/:id/toggle_favorite/  # Toggle favorito
POST   /api/routes/:id/add_review/       # Agregar reseña
```

### Categorías
```
GET    /api/categories/           # Listar categorías
```

### Favoritos
```
GET    /api/favorites/            # Mis favoritos
POST   /api/favorites/            # Agregar favorito
DELETE /api/favorites/:id/        # Eliminar favorito
```

### Chatbot
```
POST   /api/chatbot/chat/         # Enviar mensaje
GET    /api/chatbot/history/      # Historial (requiere auth)
```

---

## 🎨 Características Destacadas

### Frontend
- ✨ Diseño moderno y responsivo
- 🗺️ Mapas interactivos con Leaflet
- 🔍 Búsqueda y filtros en tiempo real
- ⭐ Sistema de calificaciones con estrellas
- ❤️ Gestión de favoritos
- 🤖 Chatbot con IA
- 🔐 Autenticación segura con JWT
- 📱 Totalmente responsive

### Backend
- 🔒 Autenticación JWT con refresh tokens
- 📊 API REST completa y documentada
- 🗄️ ORM de Django para base de datos
- 🤖 Integración con OpenAI
- 👮 Permisos granulares
- 🛡️ CORS configurado
- 📝 Panel admin completo
- ✅ Validaciones robustas

---

## 📚 Más Información

- [INSTRUCCIONES.md](INSTRUCCIONES.md) - Guía completa de instalación
- [README.md](README.md) - Descripción del proyecto
- [Frontend README](frontend/README.md) - Documentación del frontend

---

## 🎉 ¡Disfruta Explorando Ruta Local!

¿Preguntas? Revisa la documentación o el código fuente.
