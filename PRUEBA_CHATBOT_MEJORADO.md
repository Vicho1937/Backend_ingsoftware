# 🧪 Guía de Prueba - Chatbot Mejorado con Ubicación

## 🚀 Inicio Rápido

### **1. Iniciar el Sistema**

```bash
# Terminal 1 - Backend
python manage.py runserver

# Terminal 2 - Frontend  
cd frontend
npm run dev
```

### **2. Abrir el Chat**
```
http://localhost:5173/chat
```

---

## 🧪 Pruebas a Realizar

### **✅ Prueba 1: Banner de Ubicación**

**Pasos:**
1. Abre el chat sin haber dado permiso de ubicación
2. Deberías ver un banner morado con el texto:
   ```
   📍 Activa tu ubicación
   Obtén recomendaciones más precisas de lugares cercanos a ti
   [Activar Ubicación]
   ```

**Resultado Esperado:**
- ✅ Banner aparece con animación suave
- ✅ Botón "Activar Ubicación" visible
- ✅ Diseño atractivo con gradiente morado

---

### **✅ Prueba 2: Solicitud de Permiso**

**Pasos:**
1. Click en "Activar Ubicación"
2. El navegador mostrará un diálogo de permiso
3. Seleccionar "Permitir"

**Resultado Esperado:**
- ✅ Diálogo del navegador aparece
- ✅ Banner desaparece al dar permiso
- ✅ Aparece badge "📍 Ubicación activa" en el header

---

### **✅ Prueba 3: Sin Ubicación - Consulta General**

**Mensaje de Prueba:**
```
¿Qué restaurantes recomiendas?
```

**Resultado Esperado:**
- ✅ Bot menciona lugares de la categoría "Restaurante"
- ✅ Incluye nombres reales de la BD
- ✅ Menciona direcciones si están disponibles
- ✅ Sugiere activar ubicación para mejores resultados

**Ejemplo de Respuesta:**
```
Te recomiendo estos restaurantes en Santiago:

- Restaurante El Buen Sabor
  Av. Providencia 1234, Santiago
  
- La Cocina de la Abuela  
  Calle Huérfanos 890, Santiago

¿Te gustaría activar tu ubicación para encontrar 
restaurantes más cercanos a ti?
```

---

### **✅ Prueba 4: Con Ubicación - Lugares Cercanos**

**Pre-requisito:** Ubicación activa ✓

**Mensaje de Prueba:**
```
¿Qué hay cerca de mí?
```

**Resultado Esperado:**
- ✅ Bot lista lugares ordenados por distancia
- ✅ Muestra distancia en kilómetros (ej: "0.8 km")
- ✅ Incluye nombres, categorías y direcciones
- ✅ Máximo 10 lugares

**Ejemplo de Respuesta:**
```
¡Perfecto! Estos son los lugares más cercanos a ti:

📍 Restaurante El Buen Sabor (Restaurante) - A solo 0.8 km
   Av. Providencia 1234, Santiago
   Comida tradicional chilena

📍 Café Central (Café) - A 1.2 km
   Calle Merced 567, Santiago
   Café de especialidad y repostería

📍 Parque Bustamante (Parque) - A 1.5 km
   Av. Providencia con Rancagua
   Espacio verde para deportes y picnic
```

---

### **✅ Prueba 5: Búsqueda por Categoría**

**Mensajes de Prueba:**

```
1. "¿Dónde puedo tomar café?"
2. "Lugares para comer"  
3. "Parques cerca de mí"
4. "Museos en Santiago"
```

**Resultado Esperado:**
- ✅ Bot detecta la keyword (café, comer, parque, museo)
- ✅ Busca lugares de esa categoría
- ✅ Si hay ubicación, ordena por cercanía
- ✅ Si no hay ubicación, muestra los primeros 5

**Keywords que funcionan:**
| Palabra | Categoría |
|---------|-----------|
| restaurante, comida, comer | Restaurante |
| cafe, cafetería | Café |
| parque | Parque |
| museo, cultura | Museo |
| turismo | Turismo |
| hotel | Hotel |
| tienda, compras | Tienda |

---

### **✅ Prueba 6: Pregunta Específica**

**Mensaje de Prueba:**
```
Cuéntame sobre el Restaurante El Buen Sabor
```

**Resultado Esperado:**
- ✅ Bot da información detallada
- ✅ Incluye descripción del lugar
- ✅ Menciona dirección completa
- ✅ Si hay ubicación, incluye distancia

---

### **✅ Prueba 7: Denegación de Ubicación**

**Pasos:**
1. Recargar la página
2. Click en "Activar Ubicación"
3. Seleccionar "Bloquear" en el diálogo del navegador

**Resultado Esperado:**
- ✅ Banner cambia a mensaje de "Ubicación denegada"
- ✅ Sugiere activarla en configuración del navegador
- ✅ Chatbot sigue funcionando sin ubicación

---

## 🔍 Verificaciones de Backend

### **Prueba de Cálculo de Distancias:**

```bash
python manage.py shell
```

```python
from chatbot.views import calculate_distance

# Santiago Centro a Providencia (aprox 3 km)
lat1, lon1 = -33.4489, -70.6693  # Santiago Centro
lat2, lon2 = -33.4177, -70.6063  # Providencia

distance = calculate_distance(lat1, lon1, lat2, lon2)
print(f"Distancia: {distance} km")
# Esperado: ~3.0 km
```

### **Prueba de Búsqueda de Lugares:**

```python
from chatbot.views import get_nearby_places, get_places_by_category

# Buscar lugares cercanos
latitude, longitude = -33.4489, -70.6693
places = get_nearby_places(latitude, longitude, max_distance=5)
print(f"Encontrados {len(places)} lugares")

# Buscar restaurantes
restaurants = get_places_by_category('Restaurante', limit=5)
print(f"Encontrados {len(restaurants)} restaurantes")
```

---

## 📊 Casos de Uso Reales

### **Caso 1: Turista en Santiago**

```
Usuario: Hola, llegué hace poco a Santiago

Bot: ¡Bienvenido a Santiago! Soy tu asistente virtual de 
     Ruta Local. ¿Te gustaría activar tu ubicación para 
     recomendarte lugares cercanos?

Usuario: [Activa ubicación] ¿Qué lugares turísticos hay cerca?

Bot: ¡Perfecto! Estos son los lugares turísticos más cercanos:

     📍 Cerro Santa Lucía - A 0.5 km
     Parque histórico con vista panorámica de Santiago
     
     📍 Palacio de La Moneda - A 0.8 km  
     Palacio presidencial y centro histórico
     
     📍 Museo de Bellas Artes - A 1.2 km
     Principal museo de arte del país
```

### **Caso 2: Local buscando almuerzo**

```
Usuario: Tengo hambre, ¿dónde puedo almorzar?

Bot: ¡Claro! Déjame ayudarte a encontrar un buen lugar.

     📍 Restaurante El Buen Sabor - A 0.3 km (4 min caminando)
     Comida chilena tradicional, menú del día $5.000
     Av. Providencia 1234
     
     📍 Sushi Express - A 0.6 km (8 min)
     Sushi fresco, promoción de rolls 2x1
     Calle Merced 567
     
     ¿Prefieres algo en particular? ¿Comida rápida, 
     restaurante sentado, o para llevar?
```

### **Caso 3: Buscar café para trabajar**

```
Usuario: Necesito un café con wifi para trabajar

Bot: Te recomiendo estas cafeterías cercanas ideales para trabajar:

     📍 Café Central - A 0.4 km
     Wifi gratis, enchufes, ambiente tranquilo
     Horario: 8:00 - 20:00
     
     📍 Starbucks Providencia - A 0.7 km
     Wifi, aire acondicionado, segunda planta amplia
     Horario: 7:30 - 22:00
     
     Ambos lugares suelen tener mesas disponibles en la mañana.
```

---

## ⚠️ Solución de Problemas

### **Problema: Banner no aparece**

**Solución:**
1. Verificar que estás logueado
2. Refrescar la página (F5)
3. Ver consola del navegador (F12) por errores

### **Problema: Ubicación no se activa**

**Solución:**
1. Verificar permisos del navegador:
   - Chrome: Configuración → Privacidad → Configuración de sitios → Ubicación
   - Firefox: Herramientas → Configuración de página → Permisos → Ubicación
2. Verificar que el sitio use HTTPS o sea localhost
3. Intentar en modo incógnito

### **Problema: Bot no menciona lugares reales**

**Solución:**
1. Verificar que hay lugares en la BD:
   ```bash
   python manage.py shell
   from api.models import LocalRoute
   print(LocalRoute.objects.count())
   ```
2. Si es 0, cargar datos de muestra:
   ```bash
   python load_sample_data.py
   ```

### **Problema: Distancias incorrectas**

**Solución:**
1. Verificar que los lugares tienen lat/lon:
   ```python
   from api.models import LocalRoute
   places_without_coords = LocalRoute.objects.filter(
       latitude__isnull=True
   ).count()
   print(f"{places_without_coords} lugares sin coordenadas")
   ```
2. Actualizar coordenadas de lugares

---

## 📈 Métricas a Observar

### **En el Frontend:**
- ✅ Tiempo de carga del banner: < 100ms
- ✅ Tiempo para obtener ubicación: 1-3 segundos
- ✅ Badge aparece inmediatamente

### **En el Backend:**
- ✅ Cálculo de distancias: < 50ms para 1000 lugares
- ✅ Búsqueda de lugares: < 100ms
- ✅ Respuesta total del bot: 2-4 segundos (con Gemini)

### **Consola del Navegador:**
```javascript
// Ver ubicación obtenida:
Ubicación obtenida: {latitude: -33.4489, longitude: -70.6693}

// Ver payload enviado:
{
  message: "¿Qué hay cerca?",
  session_id: "session-1234567890",
  location: {latitude: -33.4489, longitude: -70.6693}
}
```

---

## ✅ Checklist de Pruebas

- [ ] Banner de ubicación aparece correctamente
- [ ] Botón de activar ubicación funciona
- [ ] Permiso del navegador se solicita
- [ ] Badge de ubicación activa aparece
- [ ] Bot da respuestas sin ubicación
- [ ] Bot calcula distancias con ubicación
- [ ] Bot ordena lugares por cercanía
- [ ] Bot detecta keywords correctamente
- [ ] Información de lugares es real (de la BD)
- [ ] Distancias son razonables (no 1000 km)
- [ ] Direcciones se muestran correctamente
- [ ] Bot sugiere activar ubicación cuando no está
- [ ] Manejo de denegación de permisos
- [ ] Estilos CSS se ven bien en mobile
- [ ] Animaciones funcionan suavemente

---

## 🎉 Resultado Esperado

Al completar todas las pruebas, deberías tener:

✅ **Un chatbot que:**
- Solicita ubicación de forma amigable
- Calcula distancias en tiempo real
- Consulta lugares reales de la BD
- Ordena recomendaciones por cercanía
- Adapta respuestas según contexto
- Detecta intenciones del usuario
- Proporciona información específica

✅ **Una experiencia de usuario:**
- Fluida y atractiva
- Personalizada según ubicación
- Útil y práctica
- Respetuosa con la privacidad

---

## 📞 Comandos Útiles

```bash
# Ver lugares en la BD
python manage.py shell
from api.models import LocalRoute
LocalRoute.objects.all().values('name', 'category__name', 'address')

# Ver categorías disponibles  
from api.models import Category
Category.objects.all().values('name')

# Probar Gemini
python test_gemini_chatbot.py

# Ver logs del backend
python manage.py runserver
# (Errores aparecen aquí)

# Ver logs del frontend
# Abrir DevTools (F12) → Console
```

---

**¡Disfruta probando el chatbot mejorado! 🚀**
