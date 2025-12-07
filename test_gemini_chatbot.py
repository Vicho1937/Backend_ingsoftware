#!/usr/bin/env python
"""
Script de prueba para el chatbot con Gemini
"""

import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno
load_dotenv()

def test_gemini_connection():
    """Probar conexión básica con Gemini"""
    print("=" * 60)
    print("🤖 PRUEBA DE CHATBOT CON GEMINI")
    print("=" * 60)
    print()
    
    # Verificar API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ Error: GEMINI_API_KEY no encontrada en .env")
        return False
    
    print(f"✅ API Key encontrada: {api_key[:20]}...")
    print()
    
    try:
        # Configurar Gemini
        genai.configure(api_key=api_key)
        print("✅ Gemini configurado correctamente")
        print()
        
        # Listar modelos disponibles
        print("📋 Modelos disponibles:")
        models = genai.list_models()
        for model in models:
            if 'generateContent' in model.supported_generation_methods:
                print(f"  - {model.name}")
        print()
        
        # Probar generación de contenido
        print("🧪 Probando generación de contenido...")
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        system_prompt = """Eres un asistente virtual especializado en la plataforma de Rutas Locales.
Tu función es ayudar a los usuarios a descubrir y obtener información sobre lugares locales, 
restaurantes, atracciones turísticas, y negocios de la zona."""
        
        test_message = "Hola, ¿qué lugares puedes recomendarme en Santiago?"
        
        full_prompt = f"{system_prompt}\n\nUsuario: {test_message}\n\nAsistente:"
        response = model.generate_content(full_prompt)
        
        print(f"✅ Respuesta generada correctamente:")
        print(f"\n{'-' * 60}")
        print(f"👤 Usuario: {test_message}")
        print(f"{'-' * 60}")
        print(f"🤖 Asistente: {response.text}")
        print(f"{'-' * 60}")
        print()
        
        print("=" * 60)
        print("✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"❌ Error durante la prueba: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_gemini_connection()
    sys.exit(0 if success else 1)
