# 🚀 Configuración de Supabase - Ruta Local

## ✅ Estado Actual: CONECTADO

El proyecto ya está configurado y conectado a Supabase PostgreSQL.

---

## 🔐 Seguridad de Credenciales

### ⚠️ IMPORTANTE: El archivo `.env` NUNCA se sube a GitHub

El archivo `.env` contiene credenciales sensibles y está protegido por `.gitignore`.

### Archivos de Configuración

- **`.env`** → Contiene tus credenciales reales (NO se sube a GitHub)
- **`.env.example`** → Plantilla sin credenciales (SÍ se sube a GitHub)
- **`.gitignore`** → Protege archivos sensibles

---

## 📋 Configuración Actual

### Variables en `.env`:
```env
# Database Configuration (Supabase)
user=postgres.aouypionjbonohgyuejj
password=Vicho1937.
host=aws-0-us-west-2.pooler.supabase.com
port=6543
dbname=postgres

# URL completa de conexión
DATABASE_URL=postgresql://[user]:[password]@[host]:[port]/[dbname]
```

### Configuración en `settings.py`:
El proyecto detecta automáticamente si existe `DATABASE_URL`:
- ✅ **Con DATABASE_URL** → Usa Supabase (PostgreSQL)
- 🔧 **Sin DATABASE_URL** → Usa SQLite local

---

## 🗄️ Estado de la Base de Datos

✅ **Migraciones aplicadas correctamente**
✅ **Tablas creadas en Supabase**
✅ **Superusuario creado** (admin / contraseña pendiente de configurar)

### Tablas creadas:
- `users` - Usuarios del sistema
- `categories` - Categorías de rutas
- `local_routes` - Rutas locales
- `reviews` - Reseñas de usuarios
- `favorites` - Favoritos de usuarios
- `chat_messages` - Historial del chatbot
- Tablas de Django (auth, sessions, admin, etc.)

---

## 🚀 Cómo usar

### 1. Configurar contraseña del superusuario
```bash
.\venv_backend\Scripts\activate
python manage.py changepassword admin
```

### 2. Cargar datos de ejemplo (opcional)
```bash
python load_sample_data.py
```

### 3. Iniciar el servidor
```bash
python manage.py runserver
```

### 4. Acceder al Admin Panel
- URL: http://localhost:8000/admin
- Usuario: `admin`
- Contraseña: (la que configuraste)

---

## 🔄 Cambiar entre SQLite y Supabase

### Para usar Supabase:
Asegúrate de que exista `DATABASE_URL` en `.env`

### Para usar SQLite local:
Comenta o elimina la línea `DATABASE_URL` en `.env`

---

## 👥 Para Colaboradores

Si alguien más clona el repositorio, debe:

1. **Copiar el archivo ejemplo:**
   ```bash
   copy .env.example .env
   ```

2. **Pedir las credenciales al propietario del proyecto**

3. **Editar `.env` con las credenciales reales**

4. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```

---

## 🔒 Verificación de Seguridad

### Verifica que `.env` esté en `.gitignore`:
```bash
git check-ignore .env
```
Debe retornar: `.env` ✅

### Verifica qué archivos se subirán a GitHub:
```bash
git status
```
**NO debe aparecer** `.env` en la lista ✅

---

## 📊 Monitoreo en Supabase

1. Ve a tu proyecto en https://supabase.com
2. **Database** → **Tables** → Ver tablas creadas
3. **Database** → **Roles** → Verificar permisos
4. **Logs** → Ver consultas y errores

---

## 🛠️ Comandos Útiles

### Ver estado de migraciones:
```bash
python manage.py showmigrations
```

### Crear nueva migración:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Acceder a shell de Django con Supabase:
```bash
python manage.py shell
```

### Hacer backup de datos:
```bash
python manage.py dumpdata > backup.json
```

### Restaurar backup:
```bash
python manage.py loaddata backup.json
```

---

## 🐛 Solución de Problemas

### Error de conexión:
- Verifica que las credenciales en `.env` sean correctas
- Verifica que Supabase esté activo en tu panel
- Revisa los logs en Supabase Dashboard

### Error "relation does not exist":
```bash
python manage.py migrate --run-syncdb
```

### Resetear base de datos (⚠️ ELIMINA TODOS LOS DATOS):
Desde Supabase Dashboard → SQL Editor:
```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
```
Luego:
```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## 📚 Recursos

- [Documentación de Supabase](https://supabase.com/docs)
- [Django Database Settings](https://docs.djangoproject.com/en/stable/ref/settings/#databases)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)

---

## ✅ Checklist de Seguridad

- [x] `.env` en `.gitignore`
- [x] `.env.example` creado
- [x] Credenciales no hardcodeadas en código
- [x] `DATABASE_URL` usando variables de entorno
- [x] README de seguridad creado

---

**🎉 ¡Tu proyecto ahora usa Supabase de forma segura!**
