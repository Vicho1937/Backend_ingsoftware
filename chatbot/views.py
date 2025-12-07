from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.conf import settings
from django.db.models import Q
import google.generativeai as genai
from .models import ChatHistory
from .serializers import ChatMessageSerializer, ChatHistorySerializer
from api.models import LocalRoute, Category
import uuid
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calcular distancia entre dos coordenadas usando Haversine"""
    R = 6371  # Radio de la Tierra en kilómetros
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lon = math.radians(lon2 - lon1)
    
    a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    distance = R * c
    return distance

def get_nearby_places(latitude, longitude, max_distance=10, limit=10):
    """Obtener lugares cercanos a una ubicación"""
    all_places = LocalRoute.objects.filter(is_active=True)
    places_with_distance = []
    
    for place in all_places:
        if place.latitude and place.longitude:
            distance = calculate_distance(
                latitude, longitude,
                float(place.latitude), float(place.longitude)
            )
            if distance <= max_distance:
                places_with_distance.append({
                    'place': place,
                    'distance': round(distance, 2)
                })
    
    # Ordenar por distancia
    places_with_distance.sort(key=lambda x: x['distance'])
    return places_with_distance[:limit]

def get_places_by_category(category_name, limit=5):
    """Buscar lugares por categoría"""
    try:
        category = Category.objects.get(name__icontains=category_name)
        places = LocalRoute.objects.filter(category=category, is_active=True)[:limit]
        return places
    except Category.DoesNotExist:
        return []

def search_places(query, limit=5):
    """Buscar lugares por nombre o descripción"""
    places = LocalRoute.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query),
        is_active=True
    )[:limit]
    return places

def clean_markdown(text):
    """Remover formato Markdown del texto"""
    import re
    # Remover negritas **texto** o __texto__
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    # Remover cursivas *texto* o _texto_
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    # Remover código `texto`
    text = re.sub(r'`(.*?)`', r'\1', text)
    return text

@api_view(['POST'])
@permission_classes([AllowAny])
def chat_message(request):
    serializer = ChatMessageSerializer(data=request.data)
    
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    user_message = serializer.validated_data['message']
    session_id = serializer.validated_data.get('session_id', str(uuid.uuid4()))
    user_location = serializer.validated_data.get('location', None)
    
    # Obtener información contextual de lugares
    context_info = ""
    
    # Si hay ubicación, buscar lugares cercanos
    if user_location:
        latitude = user_location.get('latitude')
        longitude = user_location.get('longitude')
        
        nearby_places = get_nearby_places(latitude, longitude, max_distance=10, limit=10)
        
        if nearby_places:
            context_info += "\n\n📍 LUGARES CERCANOS AL USUARIO:\n"
            for item in nearby_places:
                place = item['place']
                distance = item['distance']
                context_info += f"- {place.name} ({place.category.name if place.category else 'Sin categoría'}) - {distance} km\n"
                if place.description:
                    context_info += f"  Descripción: {place.description[:100]}...\n"
                if place.address:
                    context_info += f"  Dirección: {place.address}\n"
    
    # Buscar lugares relevantes según palabras clave del mensaje
    keywords = {
        'restaurante': 'Restaurante',
        'comida': 'Restaurante',
        'comer': 'Restaurante',
        'cafe': 'Café',
        'cafetería': 'Café',
        'parque': 'Parque',
        'museo': 'Museo',
        'cultura': 'Museo',
        'turismo': 'Turismo',
        'hotel': 'Hotel',
        'tienda': 'Tienda',
        'compras': 'Tienda'
    }
    
    for keyword, category in keywords.items():
        if keyword in user_message.lower():
            places = get_places_by_category(category, limit=5)
            if places and not context_info:
                context_info += f"\n\n🏷️ LUGARES DE {category.upper()} DISPONIBLES:\n"
                for place in places:
                    context_info += f"- {place.name}"
                    if place.address:
                        context_info += f" - {place.address}"
                    context_info += "\n"
            break
    
    # System prompt mejorado con contexto
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
    
    INSTRUCCIONES ESPECIALES:
    - Usa los datos de lugares reales proporcionados abajo para dar recomendaciones específicas
    - Si hay lugares cercanos, menciónalos con sus distancias
    - Sé específico con nombres reales de lugares, direcciones y categorías
    - Si no hay datos de ubicación, sugiere activar la ubicación para mejores recomendaciones
    
    FORMATO DE RESPUESTA:
    - NO uses formato Markdown (nada de asteriscos ** ni *)
    - Usa MAYÚSCULAS para destacar nombres de lugares en lugar de negritas
    - Usa emojis para hacer el texto más visual (📍, 🍽️, ☕, 🏛️, etc.)
    - Mantén los saltos de línea para mejor legibilidad
    - Usa guiones (-) para listas
    
    Sé amable, conciso y útil en tus respuestas."""
    
    if context_info:
        system_prompt += f"\n\n{context_info}"
    
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        full_prompt = f"{system_prompt}\n\nUsuario: {user_message}\n\nAsistente:"
        response = model.generate_content(full_prompt)
        
        # Limpiar formato Markdown de la respuesta
        bot_response = clean_markdown(response.text)
        
        # Guardar en historial
        chat_history = ChatHistory.objects.create(
            user=request.user if request.user.is_authenticated else None,
            session_id=session_id,
            message=user_message,
            response=bot_response
        )
        
        return Response({
            'session_id': session_id,
            'message': user_message,
            'response': bot_response,
            'timestamp': chat_history.created_at
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            'error': 'Error al procesar tu mensaje. Por favor intenta de nuevo.',
            'detail': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def chat_history(request):
    if not request.user.is_authenticated:
        return Response({'error': 'Debes iniciar sesión para ver tu historial'}, 
                       status=status.HTTP_401_UNAUTHORIZED)
    
    history = ChatHistory.objects.filter(user=request.user)[:20]
    serializer = ChatHistorySerializer(history, many=True)
    return Response(serializer.data)
