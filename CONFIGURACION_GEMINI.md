# 🤖 Configuración del Chatbot con Gemini - Guía Completa

## ✅ **Estado Actual**

**✅ Chatbot configurado y funcionando con Google Gemini (100% GRATIS)**

- ✅ Google Generative AI instalado (`google-generativeai==0.8.5`)
- ✅ Modelo: `gemini-2.5-flash` (último modelo gratuito de Google)
- ✅ Integración completa en backend Django
- ✅ Frontend actualizado con endpoint correcto
- ✅ Sistema de sesiones funcionando
- ✅ Historial de conversaciones guardado en base de datos
- ✅ Restricción de contexto (solo rutas locales)

---

## 🆓 **¿Por qué Gemini?**

### **Ventajas sobre OpenAI:**
- ✅ **100% GRATIS** - Sin necesidad de tarjeta de crédito
- ✅ **Sin límites de cuota** - Llamadas ilimitadas dentro de los rate limits
- ✅ **Modelo avanzado** - Gemini 2.5 Flash es uno de los modelos más recientes
- ✅ **Multimodal** - Soporta texto, imágenes, audio y video
- ✅ **Rápido** - Latencia muy baja en respuestas
- ✅ **API simple** - Fácil de usar y mantener

### **Rate Limits (Plan Gratuito):**
- 15 requests por minuto (RPM)
- 1 millón de tokens por minuto (TPM)
- 1,500 requests por día (RPD)

**Para el proyecto de Rutas Locales, estos límites son más que suficientes.**

---

## 🔑 **Configuración Actual**

### **1. API Key en `.env`:**
```env
GEMINI_API_KEY=AIzaSyDeSGpw8EpEhKum3hNfO3yhOt5IXGl9a9o
```

### **2. Configuración en `settings.py`:**
```python
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
```

### **3. Código del Chatbot (`chatbot/views.py`):**
```python
import google.generativeai as genai

# En la vista chat_message:
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

full_prompt = f"{system_prompt}\n\nUsuario: {user_message}\n\nAsistente:"
response = model.generate_content(full_prompt)

bot_response = response.text
```

---

## 🚀 **Cómo Obtener una API Key de Gemini**

### **Paso a Paso:**

1. **Ve a Google AI Studio:**
   - URL: https://aistudio.google.com/app/apikey

2. **Inicia sesión con tu cuenta de Google**
   - Usa cualquier cuenta de Gmail

3. **Crear API Key:**
   - Click en **"Get API Key"** o **"Create API Key"**
   - Selecciona tu proyecto de Google Cloud (o crea uno nuevo)
   - La key se genera instantáneamente

4. **Copiar la Key:**
   - Formato: `AIzaSy...` (39 caracteres)
   - Guárdala en un lugar seguro

5. **Agregar al `.env`:**
   ```env
   GEMINI_API_KEY=tu-key-aqui
   ```

**⚠️ Importante:**
- No compartas tu API key con nadie
- No la subas a GitHub (ya está en `.gitignore`)
- Puedes regenerarla en cualquier momento si se compromete

---

## 📊 **Modelos Disponibles (Gratuitos)**

### **Recomendados para Chat:**

| Modelo | Descripción | Velocidad | Calidad |
|--------|-------------|-----------|---------|
| `gemini-2.5-flash` | **⭐ Recomendado** - Último modelo, rápido y preciso | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| `gemini-2.5-pro` | Más potente, respuestas más elaboradas | ⚡⚡ | ⭐⭐⭐⭐⭐ |
| `gemini-2.0-flash` | Versión anterior, muy estable | ⚡⚡⚡ | ⭐⭐⭐⭐ |
| `gemini-flash-latest` | Siempre apunta al último modelo flash | ⚡⚡⚡ | ⭐⭐⭐⭐ |

### **Actualmente usando:** `gemini-2.5-flash`

---

## 🧪 **Probar el Chatbot**

### **1. Desde la línea de comandos:**
```bash
python test_gemini_chatbot.py
```

Este script verifica:
- ✅ API Key configurada correctamente
- ✅ Conexión con Gemini
- ✅ Modelos disponibles
- ✅ Generación de respuestas

### **2. Desde el frontend:**
1. Inicia el backend:
   ```bash
   python manage.py runserver
   ```

2. Inicia el frontend:
   ```bash
   cd frontend
   npm run dev
   ```

3. Ve a: http://localhost:5173/chat
4. Inicia sesión si es necesario
5. ¡Prueba el chatbot!

### **3. Con curl (API directa):**
```bash
curl -X POST http://localhost:8000/api/chatbot/message/ \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Hola, ¿qué lugares puedo visitar?\"}"
```

---

## 📝 **Estructura del Proyecto**

### **Backend:**
```
chatbot/
├── models.py          # Modelo ChatHistory
├── views.py           # Lógica del chatbot con Gemini
├── serializers.py     # Serializadores
└── urls.py            # Endpoints: /message/, /history/
```

### **Frontend:**
```
src/
└── pages/
    └── Chat.jsx       # Interfaz del chatbot
```

### **Configuración:**
```
.env                   # GEMINI_API_KEY
settings.py            # Configuración Django
requirements.txt       # Dependencias (google-generativeai)
```

---

## 🎨 **Personalización del Chatbot**

### **System Prompt Actual:**
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

### **Cambiar el Modelo:**
En `chatbot/views.py`, línea 41:
```python
model = genai.GenerativeModel('gemini-2.5-flash')
# Cambia a:
# model = genai.GenerativeModel('gemini-2.5-pro')  # Más potente
# model = genai.GenerativeModel('gemini-2.0-flash') # Más estable
```

### **Ajustar Parámetros:**
```python
generation_config = {
    "temperature": 0.7,      # Creatividad (0.0 - 1.0)
    "top_p": 0.8,           # Diversidad de respuestas
    "top_k": 40,            # Número de tokens considerados
    "max_output_tokens": 500, # Longitud máxima de respuesta
}

response = model.generate_content(
    full_prompt,
    generation_config=generation_config
)
```

---

## 🔒 **Seguridad**

### **1. API Key:**
- ✅ Guardada en `.env` (no en el código)
- ✅ `.env` está en `.gitignore`
- ✅ No se expone en el frontend

### **2. Rate Limiting (Recomendado agregar):**
```python
from django.core.cache import cache

# En chat_message view:
user_key = f"chat_rate_{request.user.id}"
request_count = cache.get(user_key, 0)

if request_count >= 10:  # Máximo 10 mensajes por minuto
    return Response({
        'error': 'Demasiadas solicitudes. Espera un momento.'
    }, status=status.HTTP_429_TOO_MANY_REQUESTS)

cache.set(user_key, request_count + 1, 60)
```

### **3. Validación de Entrada:**
```python
if len(user_message) > 1000:
    return Response({
        'error': 'Mensaje demasiado largo'
    }, status=status.HTTP_400_BAD_REQUEST)
```

---

## 📈 **Monitoreo y Logs**

### **Ver uso en Google AI Studio:**
- URL: https://aistudio.google.com/app/apikey
- Click en tu API key
- Ver estadísticas de uso

### **Logs en Django:**
```python
import logging
logger = logging.getLogger(__name__)

# En chat_message:
logger.info(f"Chat request from user {request.user.id}: {user_message[:50]}")
logger.info(f"Chat response length: {len(bot_response)} chars")
```

---

## 🐛 **Troubleshooting**

### **Error: "API key not valid"**
```bash
# Verifica que la key esté en .env
cat .env | grep GEMINI_API_KEY

# Reinicia el servidor Django
python manage.py runserver
```

### **Error: "Resource has been exhausted"**
- Has excedido el rate limit (15 req/min)
- Espera 1 minuto y vuelve a intentar
- Considera agregar rate limiting

### **Error: "Model not found"**
```python
# Lista modelos disponibles:
python -c "import google.generativeai as genai; import os; from dotenv import load_dotenv; load_dotenv(); genai.configure(api_key=os.getenv('GEMINI_API_KEY')); [print(m.name) for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]"
```

### **El bot responde en inglés:**
Agrega al system prompt:
```python
"IMPORTANTE: Responde SIEMPRE en español."
```

---

## 🚀 **Mejoras Futuras (Opcionales)**

### **1. Mantener Contexto de Conversación:**
```python
# Obtener últimos 5 mensajes
previous_messages = ChatHistory.objects.filter(
    session_id=session_id
).order_by('-created_at')[:5]

# Construir historial
conversation_history = ""
for msg in reversed(previous_messages):
    conversation_history += f"Usuario: {msg.message}\nAsistente: {msg.response}\n\n"

full_prompt = f"{system_prompt}\n\nHistorial:\n{conversation_history}\nUsuario: {user_message}\n\nAsistente:"
```

### **2. Integrar con Base de Datos:**
```python
from api.models import LocalRoute

# Buscar lugares relevantes
routes = LocalRoute.objects.filter(name__icontains=search_term)[:5]
routes_info = "\n".join([f"- {r.name}: {r.description}" for r in routes])

system_prompt += f"\n\nLugares disponibles:\n{routes_info}"
```

### **3. Soporte Multimodal (Imágenes):**
```python
# Si el usuario sube una imagen:
import PIL.Image

img = PIL.Image.open('lugar.jpg')
response = model.generate_content([user_message, img])
```

### **4. Streaming de Respuestas:**
```python
response = model.generate_content(full_prompt, stream=True)

for chunk in response:
    if chunk.text:
        yield chunk.text  # Enviar palabra por palabra
```

---

## ✅ **Checklist de Implementación**

- [x] API Key de Gemini configurada en `.env`
- [x] `google-generativeai` instalado
- [x] Backend actualizado para usar Gemini
- [x] Frontend actualizado con endpoint correcto
- [x] Modelo `gemini-2.5-flash` configurado
- [x] System prompt personalizado
- [x] Historial de chat en base de datos
- [x] Manejo de errores implementado
- [x] Script de prueba creado
- [ ] Rate limiting agregado (opcional)
- [ ] Contexto de conversación (opcional)
- [ ] Integración con lugares de la BD (opcional)

---

## 📞 **Recursos Útiles**

- **Google AI Studio:** https://aistudio.google.com/
- **Documentación Gemini:** https://ai.google.dev/docs
- **Playground:** https://aistudio.google.com/prompts/new_chat
- **Precios y Límites:** https://ai.google.dev/pricing
- **Guías de Gemini:** https://ai.google.dev/gemini-api/docs

---

## 🎉 **Resultado Final**

El chatbot ahora funciona con **Google Gemini completamente gratis**, sin necesidad de tarjeta de crédito ni preocupaciones por costos. Puede:

✅ Responder preguntas sobre lugares locales
✅ Dar recomendaciones personalizadas
✅ Ayudar a los usuarios con la plataforma
✅ Mantener historial de conversaciones
✅ Rechazar preguntas fuera de contexto
✅ Funcionar para usuarios logueados y no logueados

**¡El chatbot está listo para usar! 🚀**
