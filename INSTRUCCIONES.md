# 📍 Ruta Local - Instrucciones de Instalación y Uso

## 🚀 Proyecto Completo

Este proyecto es una plataforma web fullstack para descubrir y compartir rutas locales, con las siguientes características:

### ✨ Características Principales

- **Backend Django REST Framework**
  - Autenticación JWT
  - API RESTful completa
  - Sistema de rutas y categorías
  - Reseñas y calificaciones
  - Sistema de favoritos
  - Chatbot con OpenAI
  - Panel de administración

- **Frontend React**
  - Interfaz moderna y responsiva
  - Exploración de rutas
  - Visualización en mapas interactivos
  - Chat con IA
  - Gestión de perfil
  - Sistema de favoritos

---

## 📋 Requisitos Previos

- Python 3.10 o superior
- Node.js 18 o superior
- SQLite (incluido con Python)

---

## 🔧 Instalación del Backend

### 1. Activar el entorno virtual

```bash
cd Backend_ingsoftware
.\venv_backend\Scripts\activate
```

### 2. Instalar dependencias (si no están instaladas)

```bash
pip install django djangorestframework djangorestframework-simplejwt django-cors-headers django-filter python-dotenv openai
```

### 3. Configurar variables de entorno

Edita el archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-clave-secreta-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
OPENAI_API_KEY=tu-clave-api-openai
```

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu usuario administrador.

### 6. Cargar datos de ejemplo (opcional)

Puedes crear categorías desde el panel admin o usar el shell:

```bash
python manage.py shell
```

```python
from api.models import Category

categories = [
    {'name': 'Restaurantes', 'icon': '🍽️', 'description': 'Los mejores lugares para comer'},
    {'name': 'Turismo', 'icon': '🏛️', 'description': 'Lugares turísticos y atracciones'},
    {'name': 'Entretenimiento', 'icon': '🎭', 'description': 'Cines, teatros y más'},
    {'name': 'Parques', 'icon': '🌳', 'description': 'Espacios verdes y recreativos'},
    {'name': 'Museos', 'icon': '🖼️', 'description': 'Arte y cultura'},
    {'name': 'Cafeterías', 'icon': '☕', 'description': 'Café y lugares acogedores'},
]

for cat in categories:
    Category.objects.get_or_create(**cat)

exit()
```

### 7. Ejecutar el servidor backend

```bash
python manage.py runserver
```

El backend estará disponible en: **http://localhost:8000**

- Panel Admin: **http://localhost:8000/admin**
- API: **http://localhost:8000/api/**

---

## 🎨 Instalación del Frontend

### 1. Navegar a la carpeta frontend

```bash
cd frontend
```

### 2. Instalar dependencias

```bash
npm install
```

### 3. Configurar variables de entorno (opcional)

Crea un archivo `.env` si quieres personalizar la URL del API:

```env
VITE_API_URL=http://localhost:8000/api
```

### 4. Ejecutar el servidor de desarrollo

```bash
npm run dev
```

El frontend estará disponible en: **http://localhost:5173**

---

## 📱 Uso de la Aplicación

### Para Usuarios

1. **Registro/Login**
   - Ve a http://localhost:5173
   - Crea una cuenta o inicia sesión

2. **Explorar Rutas**
   - Navega por las rutas disponibles
   - Filtra por categoría
   - Busca lugares específicos
   - Visualiza en el mapa

3. **Detalles de Ruta**
   - Ver información completa
   - Ver ubicación en mapa
   - Leer y escribir reseñas
   - Agregar a favoritos

4. **Chatbot**
   - Pregunta sobre lugares
   - Obtén recomendaciones
   - Ayuda sobre la plataforma

5. **Perfil**
   - Edita tu información
   - Ve tus estadísticas
   - Gestiona favoritos

### Para Administradores

1. **Acceder al Panel Admin**
   - Ve a http://localhost:8000/admin
   - Inicia sesión con tu superusuario

2. **Gestionar Contenido**
   - Crear/Editar categorías
   - Crear/Editar rutas
   - Moderar reseñas
   - Gestionar usuarios

---

## 🗂️ Estructura del Proyecto

```
Backend_ingsoftware/
├── api/                      # App principal de rutas
│   ├── models.py            # Modelos (Category, LocalRoute, Review, Favorite)
│   ├── views.py             # Vistas API
│   ├── serializers.py       # Serializers REST
│   └── urls.py              # URLs de API
├── authentication/           # Sistema de autenticación
│   ├── models.py            # Modelo User personalizado
│   ├── views.py             # Login, register, profile
│   └── serializers.py       # Serializers de usuario
├── chatbot/                 # Sistema de chatbot
│   ├── models.py            # Historial de chat
│   ├── views.py             # Integración con OpenAI
│   └── urls.py              # URLs del chatbot
├── ruta_local_backend/      # Configuración Django
│   ├── settings.py          # Configuración principal
│   └── urls.py              # URLs principales
├── frontend/                # Aplicación React
│   ├── src/
│   │   ├── components/      # Componentes reutilizables
│   │   ├── pages/           # Páginas de la app
│   │   ├── services/        # API service (axios)
│   │   ├── context/         # Context API (Auth)
│   │   └── styles/          # CSS por componente
│   ├── public/
│   └── package.json
├── db.sqlite3               # Base de datos SQLite
├── manage.py                # Django management
└── requirements.txt         # Dependencias Python
```

---

## 🔌 Endpoints del API

### Autenticación
- `POST /api/auth/register/` - Registro
- `POST /api/auth/login/` - Login (usa token endpoint)
- `POST /api/auth/token/` - Obtener tokens JWT
- `POST /api/auth/token/refresh/` - Refrescar token
- `GET /api/auth/profile/` - Ver perfil
- `PUT /api/auth/profile/` - Actualizar perfil
- `POST /api/auth/logout/` - Cerrar sesión

### Rutas
- `GET /api/routes/` - Listar rutas
- `GET /api/routes/:id/` - Detalle de ruta
- `POST /api/routes/` - Crear ruta (admin)
- `PUT /api/routes/:id/` - Actualizar ruta (admin)
- `DELETE /api/routes/:id/` - Eliminar ruta (admin)
- `POST /api/routes/:id/toggle_favorite/` - Toggle favorito
- `POST /api/routes/:id/add_review/` - Agregar reseña

### Categorías
- `GET /api/categories/` - Listar categorías
- `GET /api/categories/:id/` - Detalle de categoría
- `POST /api/categories/` - Crear categoría (admin)

### Favoritos
- `GET /api/favorites/` - Mis favoritos
- `POST /api/favorites/` - Agregar favorito
- `DELETE /api/favorites/:id/` - Eliminar favorito

### Reseñas
- `GET /api/reviews/` - Listar reseñas
- `GET /api/reviews/?route=:id` - Reseñas de una ruta

### Chatbot
- `POST /api/chatbot/chat/` - Enviar mensaje al chatbot
- `GET /api/chatbot/history/` - Historial de chat

---

## 🧪 Testing

### Backend
```bash
python manage.py test
```

### Frontend
```bash
cd frontend
npm run test
```

---

## 🐛 Solución de Problemas

### El backend no inicia
- Verifica que el entorno virtual esté activado
- Verifica que todas las dependencias estén instaladas
- Verifica que las migraciones estén aplicadas

### El frontend no inicia
- Verifica que Node.js esté instalado
- Elimina `node_modules` y ejecuta `npm install` nuevamente
- Verifica que el puerto 5173 esté disponible

### Error de CORS
- Verifica que el frontend esté en la lista de `CORS_ALLOWED_ORIGINS` en settings.py

### Chatbot no funciona
- Verifica que tengas una clave de OpenAI válida en `.env`
- La clave debe tener créditos disponibles

---

## 📚 Recursos Adicionales

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Leaflet Documentation](https://leafletjs.com/)

---

## 👥 Desarrollo

Este proyecto fue desarrollado como parte del curso de Ingeniería de Software.

### Próximas Mejoras

- [ ] Deploy en producción (Railway/Vercel)
- [ ] Integración con PostgreSQL/Supabase
- [ ] Upload de imágenes
- [ ] Sistema de notificaciones
- [ ] Rutas personalizadas por usuario
- [ ] Integración con redes sociales
- [ ] PWA (Progressive Web App)

---

## 📄 Licencia

Este proyecto es para uso educativo.
