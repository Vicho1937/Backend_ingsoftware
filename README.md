# 🗺️ Ruta Local - Plataforma de Descubrimiento de Lugares

> Plataforma web fullstack para descubrir, compartir y explorar rutas locales con integración de mapas y chatbot con IA.

## 📋 Descripción

Ruta Local es una aplicación web completa que permite a los usuarios descubrir lugares interesantes en su ciudad, dejar reseñas, guardar favoritos y obtener recomendaciones personalizadas a través de un chatbot inteligente.

## ✨ Características Principales

### Backend (Django REST Framework)
- ✅ **Autenticación JWT** - Sistema completo de registro, login y gestión de sesiones
- ✅ **API RESTful** - Endpoints bien documentados y organizados
- ✅ **Gestión de Rutas** - CRUD completo con categorización
- ✅ **Sistema de Reseñas** - Calificaciones y comentarios por usuario
- ✅ **Favoritos** - Guarda tus lugares preferidos
- ✅ **Chatbot con IA** - Integración con OpenAI para asistencia inteligente
- ✅ **Panel Admin** - Interfaz administrativa completa
- ✅ **Base de datos SQLite** - Configuración local lista para desarrollo

### Frontend (React + Vite)
- ✅ **Interfaz Moderna** - Diseño responsivo y atractivo
- ✅ **Mapas Interactivos** - Visualización con Leaflet
- ✅ **Búsqueda y Filtros** - Encuentra lugares fácilmente
- ✅ **Chat con IA** - Asistente virtual integrado
- ✅ **Gestión de Perfil** - Edita tu información personal
- ✅ **Sistema de Favoritos** - Marca y gestiona tus lugares preferidos
- ✅ **Reseñas y Calificaciones** - Comparte tu experiencia

## 🚀 Inicio Rápido

### Opción 1: Scripts Automáticos (Windows)

1. **Setup Inicial** (solo la primera vez)
```bash
setup_inicial.bat
```

2. **Iniciar Backend**
```bash
start_backend.bat
```

3. **Iniciar Frontend** (en otra terminal)
```bash
start_frontend.bat
```

### Opción 2: Manual

Ver [INSTRUCCIONES.md](INSTRUCCIONES.md) para instalación paso a paso.

## 📱 URLs de Acceso

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000/api/
- **Panel Admin**: http://localhost:8000/admin

## 🛠️ Tecnologías Utilizadas

### Backend
- Django 6.0
- Django REST Framework
- Simple JWT
- Django CORS Headers
- Django Filters
- OpenAI API
- SQLite

### Frontend
- React 18
- React Router DOM
- Axios
- Leaflet / React-Leaflet
- Vite

## 📂 Estructura del Proyecto

```
Backend_ingsoftware/
├── api/                    # App de rutas y lugares
├── authentication/         # Sistema de usuarios
├── chatbot/               # Integración con OpenAI
├── ruta_local_backend/    # Configuración Django
├── frontend/              # Aplicación React
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── context/
│   │   └── styles/
│   └── package.json
├── db.sqlite3            # Base de datos
├── manage.py
└── requirements.txt
```

## 🔧 Configuración

### Variables de Entorno (.env)

```env
SECRET_KEY=tu-clave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
OPENAI_API_KEY=tu-api-key-de-openai
```

## 📚 Documentación

- [Instrucciones Completas](INSTRUCCIONES.md)
- [Frontend README](frontend/README.md)

## 🎯 Funcionalidades Implementadas

- [x] Sistema de autenticación completo
- [x] CRUD de rutas locales
- [x] Sistema de categorías
- [x] Reseñas y calificaciones
- [x] Favoritos por usuario
- [x] Búsqueda y filtros avanzados
- [x] Visualización en mapas
- [x] Chatbot con OpenAI
- [x] Panel de administración
- [x] Responsive design
- [x] API RESTful completa

## 🔜 Mejoras Futuras

- [ ] Upload de imágenes
- [ ] Sistema de notificaciones
- [ ] Compartir en redes sociales
- [ ] Rutas personalizadas por usuario
- [ ] PWA (Progressive Web App)
- [ ] Deploy en producción

## 👥 Desarrollo

Proyecto desarrollado para el curso de Ingeniería de Software.

## 📄 Licencia

Este proyecto es para uso educativo.
Project evaluations
