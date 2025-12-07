# 🤖 Configuración del Chatbot - Guía Completa

## 📋 **Estado Actual**

✅ **Ya configurado:**
- ✅ Modelos de base de datos (ChatHistory)
- ✅ Vistas y endpoints (`/chatbot/message/`, `/chatbot/history/`)
- ✅ Integración con OpenAI GPT-3.5-turbo
- ✅ Sistema de sesiones
- ✅ Historial de chat
- ✅ Restricción de contexto (solo rutas locales)
- ✅ Librería `openai==2.9.0` en requirements.txt

❌ **Falta configurar:**
- ❌ API Key de OpenAI en `.env`

---

## 🔑 **Paso 1: Obtener API Key de OpenAI**

### **Opción A: Si ya tienes cuenta en OpenAI**
1. Ve a https://platform.openai.com/api-keys
2. Inicia sesión con tu cuenta
3. Click en "Create new secret key"
4. Copia la key (empieza con `sk-...`)

### **Opción B: Crear cuenta nueva**
1. Ve a https://platform.openai.com/signup
2. Regístrate con email o Google
3. Verifica tu cuenta
4. Ve a "API Keys" en el menú
5. Click en "Create new secret key"
6. Copia la key

### **💰 Importante sobre costos:**
- **GPT-3.5-turbo** es muy económico:
  - ~$0.002 por cada 1,000 tokens
  - Una conversación típica: ~500 tokens
  - **Costo por conversación: ~$0.001 (menos de 1 centavo)**
  
- **Créditos gratuitos:**
  - Cuentas nuevas reciben **$5 USD gratis**
  - Suficiente para ~5,000 conversaciones
  - Válido por 3 meses

---

## 🔧 **Paso 2: Configurar la API Key**

### **Edita el archivo `.env`:**

```bash
# Abre el archivo .env en el directorio raíz del proyecto
C:\Users\Vicente\Documents\GitHub\Backend_ingsoftware\.env
```

### **Reemplaza esta línea:**
```env
OPENAI_API_KEY=your_openai_api_key
```

### **Con tu key real:**
```env
OPENAI_API_KEY=sk-tu-key-real-aqui-12345678901234567890
```

**⚠️ IMPORTANTE:**
- NO compartas esta key con nadie
- NO la subas a GitHub
- El archivo `.env` debe estar en `.gitignore`

---

## 🗄️ **Paso 3: Migrar la Base de Datos**

El modelo `ChatHistory` necesita estar en la base de datos:

```bash
# 1. Asegúrate de que el backend esté parado
# 2. Ejecuta las migraciones

python manage.py makemigrations chatbot
python manage.py migrate chatbot
```

**O si prefieres migrar todo:**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ✅ **Paso 4: Verificar la Instalación**

### **Verifica que openai esté instalado:**
```bash
pip list | findstr openai
```

**Deberías ver:**
```
openai    2.9.0
```

**Si no está instalado:**
```bash
pip install openai==2.9.0
```

---

## 🧪 **Paso 5: Probar el Chatbot**

### **1. Inicia el backend:**
```bash
python manage.py runserver
```

### **2. Prueba el endpoint con curl:**
```bash
curl -X POST http://localhost:8000/chatbot/message/ \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Hola, ¿qué lugares puedo visitar en Santiago?\"}"
```

### **3. O prueba desde el frontend:**
```bash
# En otra terminal, inicia el frontend
cd frontend
npm run dev
```

Luego ve a: `http://localhost:5173/chat`

---

## 📝 **Estructura del Chatbot Actual**

### **Modelo de Datos:**
```python
class ChatHistory(models.Model):
    user = models.ForeignKey(...)  # Usuario (puede ser null)
    session_id = models.CharField(max_length=100)
    message = models.TextField()  # Mensaje del usuario
    response = models.TextField()  # Respuesta del bot
    created_at = models.DateTimeField(auto_now_add=True)
```

### **Endpoints:**

1. **POST `/api/chatbot/message/`**
   ```json
   Request:
   {
     "message": "¿Qué restaurantes recomiendas?",
     "session_id": "opcional-uuid-aqui"
   }

   Response:
   {
     "session_id": "uuid-de-sesion",
     "message": "¿Qué restaurantes recomiendas?",
     "response": "Te recomiendo estos restaurantes...",
     "timestamp": "2024-12-06T20:00:00Z"
   }
   ```

2. **GET `/api/chatbot/history/`** (requiere autenticación)
   - Devuelve las últimas 20 conversaciones del usuario

---

## 🎯 **Configuración del System Prompt**

El chatbot está configurado con un prompt especializado:

```python
system_prompt = """Eres un asistente virtual especializado en la plataforma de Rutas Locales.
Tu función es ayudar a los usuarios a descubrir y obtener información sobre lugares locales, 
restaurantes, atracciones turísticas, y negocios de la zona.

IMPORTANTE: Solo debes responder preguntas relacionadas con:
- Información sobre rutas y lugares locales
- Cómo usar la plataforma
- Recomendaciones de lugares
- Características de la aplicación
- Ayuda para navegar por la plataforma

Si te hacen una pregunta que NO está relacionada con estos temas, debes responder amablemente:
"Lo siento, solo puedo ayudarte con información sobre rutas locales y el uso de esta plataforma. 
¿Hay algo específico sobre lugares locales que te gustaría saber?"

Sé amable, conciso y útil en tus respuestas."""
```

---

## 🔒 **Seguridad y Mejores Prácticas**

### **1. Protección de API Key:**
```python
# ✅ CORRECTO - Usando variable de entorno
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')

# ❌ INCORRECTO - Nunca hagas esto
OPENAI_API_KEY = 'sk-hardcoded-key-here'
```

### **2. Límites de Tokens:**
```python
max_tokens=500  # Limita el costo por respuesta
```

### **3. Rate Limiting (recomendado):**
Considera agregar:
```python
from django.core.cache import cache
from django.utils import timezone

# En la vista chat_message:
user_key = f"chat_rate_{request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')}"
request_count = cache.get(user_key, 0)

if request_count >= 10:  # Máximo 10 mensajes por minuto
    return Response({
        'error': 'Demasiadas solicitudes. Por favor espera un momento.'
    }, status=status.HTTP_429_TOO_MANY_REQUESTS)

cache.set(user_key, request_count + 1, 60)  # Expira en 60 segundos
```

---

## 🎨 **Mejoras Futuras (Opcionales)**

### **1. Contexto de Conversación:**
Actualmente cada mensaje es independiente. Para mantener contexto:

```python
# Obtener últimos 5 mensajes de la sesión
previous_messages = ChatHistory.objects.filter(
    session_id=session_id
).order_by('-created_at')[:5]

messages = [{"role": "system", "content": system_prompt}]
for msg in reversed(previous_messages):
    messages.append({"role": "user", "content": msg.message})
    messages.append({"role": "assistant", "content": msg.response})
messages.append({"role": "user", "content": user_message})
```

### **2. Integración con Base de Datos:**
Hacer que el chatbot consulte lugares reales:

```python
from api.models import LocalRoute

# En el system prompt, agregar:
available_routes = LocalRoute.objects.filter(is_active=True).values('name', 'category__name', 'address')
routes_info = "\n".join([f"- {r['name']} ({r['category__name']}): {r['address']}" for r in available_routes[:10]])

system_prompt += f"\n\nLugares disponibles en la base de datos:\n{routes_info}"
```

### **3. Embeddings para Búsqueda Semántica:**
```python
from openai import OpenAI

# Crear embeddings de lugares
def create_route_embedding(route):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    text = f"{route.name} {route.description} {route.category.name}"
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response.data[0].embedding

# Buscar lugares similares a la pregunta del usuario
```

### **4. Streaming de Respuestas:**
Para respuestas más rápidas (palabra por palabra):

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    stream=True  # Activar streaming
)

for chunk in response:
    if chunk.choices[0].delta.content:
        yield chunk.choices[0].delta.content
```

---

## 📊 **Monitoreo de Costos**

### **Ver uso en OpenAI:**
1. Ve a https://platform.openai.com/usage
2. Verás:
   - Requests por día
   - Tokens usados
   - Costo estimado

### **Límites recomendados:**
```python
# En settings.py
CHATBOT_MAX_TOKENS = 500
CHATBOT_TEMPERATURE = 0.7
CHATBOT_MAX_MESSAGES_PER_USER = 100  # Por día
```

---

## 🐛 **Troubleshooting**

### **Error: "OpenAI API key not found"**
```bash
# Verifica que la key esté en .env
cat .env | grep OPENAI_API_KEY

# Reinicia el servidor Django
python manage.py runserver
```

### **Error: "RateLimitError"**
- Has excedido el límite de requests
- Espera un minuto y vuelve a intentar
- Considera actualizar tu plan en OpenAI

### **Error: "Invalid API Key"**
- Verifica que la key sea correcta
- Asegúrate de copiar toda la key (empieza con `sk-`)
- Genera una nueva key en OpenAI

### **El bot responde cosas no relacionadas:**
- Ajusta el `system_prompt` en `views.py`
- Reduce la `temperature` (0.5 = más determinístico)

---

## ✅ **Checklist Final**

Antes de probar:
- [ ] API Key de OpenAI configurada en `.env`
- [ ] `openai==2.9.0` instalado
- [ ] Migraciones ejecutadas
- [ ] Backend corriendo en puerto 8000
- [ ] Frontend corriendo en puerto 5173
- [ ] Archivo `.env` en `.gitignore`

---

## 🎯 **Comandos Rápidos**

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Migrar base de datos
python manage.py migrate

# 3. Iniciar backend
python manage.py runserver

# 4. En otra terminal, iniciar frontend
cd frontend
npm run dev

# 5. Probar chatbot
# Ve a http://localhost:5173/chat
```

---

## 🚀 **Resultado Final**

Una vez configurado, el chatbot podrá:
- ✅ Responder preguntas sobre lugares locales
- ✅ Dar recomendaciones personalizadas
- ✅ Explicar cómo usar la plataforma
- ✅ Mantener historial de conversaciones
- ✅ Rechazar preguntas fuera de contexto
- ✅ Funcionar para usuarios logueados y no logueados

---

## 📞 **Soporte**

Si tienes problemas:
1. Revisa los logs del backend
2. Verifica la consola del navegador (F12)
3. Confirma que la API key sea válida
4. Asegúrate de tener créditos en tu cuenta de OpenAI

¡Listo para conversar! 🤖💬
