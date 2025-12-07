#!/usr/bin/env python
"""
Script de verificación del Chatbot
Verifica que todo esté configurado correctamente
"""

import os
import sys
from pathlib import Path

def print_status(message, status):
    """Imprime estado con colores"""
    symbols = {'ok': '✅', 'error': '❌', 'warning': '⚠️', 'info': 'ℹ️'}
    print(f"{symbols.get(status, 'ℹ️')} {message}")

def check_env_file():
    """Verifica el archivo .env"""
    print("\n📋 Verificando archivo .env...")
    
    if not Path('.env').exists():
        print_status("Archivo .env no encontrado", 'error')
        return False
    
    print_status("Archivo .env encontrado", 'ok')
    
    with open('.env', 'r') as f:
        content = f.read()
        
    if 'OPENAI_API_KEY=' not in content:
        print_status("Variable OPENAI_API_KEY no encontrada en .env", 'error')
        return False
    
    # Extraer la key
    for line in content.split('\n'):
        if line.startswith('OPENAI_API_KEY='):
            key = line.split('=', 1)[1].strip()
            if key in ['', 'your_openai_api_key', 'sk-...']:
                print_status("OPENAI_API_KEY no está configurada (usando placeholder)", 'error')
                print("   🔑 Necesitas obtener una API Key de OpenAI")
                print("   🌐 Visita: https://platform.openai.com/api-keys")
                return False
            
            if not key.startswith('sk-'):
                print_status("OPENAI_API_KEY parece inválida (debe empezar con 'sk-')", 'warning')
            else:
                print_status(f"OPENAI_API_KEY configurada: {key[:15]}...", 'ok')
                return True
    
    return False

def check_openai_package():
    """Verifica que openai esté instalado"""
    print("\n📦 Verificando paquete openai...")
    
    try:
        import openai
        version = openai.__version__
        print_status(f"openai {version} instalado correctamente", 'ok')
        return True
    except ImportError:
        print_status("Paquete openai NO instalado", 'error')
        print("   📥 Ejecuta: pip install openai==2.9.0")
        return False

def check_migrations():
    """Verifica las migraciones"""
    print("\n🗄️  Verificando migraciones...")
    
    migrations_path = Path('chatbot/migrations')
    if not migrations_path.exists():
        print_status("Directorio de migraciones no encontrado", 'error')
        return False
    
    migration_files = list(migrations_path.glob('*.py'))
    migration_files = [f for f in migration_files if f.name != '__init__.py']
    
    if not migration_files:
        print_status("No se encontraron archivos de migración", 'warning')
        print("   🔧 Ejecuta: python manage.py makemigrations chatbot")
        return False
    
    print_status(f"Encontradas {len(migration_files)} migraciones", 'ok')
    return True

def check_settings():
    """Verifica settings.py"""
    print("\n⚙️  Verificando configuración...")
    
    try:
        sys.path.insert(0, str(Path.cwd()))
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruta_local_backend.settings')
        
        import django
        django.setup()
        
        from django.conf import settings
        
        if hasattr(settings, 'OPENAI_API_KEY'):
            print_status("OPENAI_API_KEY configurada en settings.py", 'ok')
        else:
            print_status("OPENAI_API_KEY NO encontrada en settings.py", 'error')
            return False
        
        return True
        
    except Exception as e:
        print_status(f"Error al verificar settings: {e}", 'error')
        return False

def check_chatbot_app():
    """Verifica que la app chatbot exista"""
    print("\n🤖 Verificando app chatbot...")
    
    required_files = [
        'chatbot/__init__.py',
        'chatbot/models.py',
        'chatbot/views.py',
        'chatbot/urls.py',
        'chatbot/serializers.py',
    ]
    
    all_exist = True
    for file_path in required_files:
        if Path(file_path).exists():
            print_status(f"{file_path} ✓", 'ok')
        else:
            print_status(f"{file_path} NO encontrado", 'error')
            all_exist = False
    
    return all_exist

def test_openai_connection():
    """Prueba la conexión con OpenAI"""
    print("\n🌐 Probando conexión con OpenAI...")
    
    try:
        from openai import OpenAI
        from django.conf import settings
        
        client = OpenAI(api_key=settings.OPENAI_API_KEY)
        
        # Hacer una prueba simple
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": "Di 'funciona' si me puedes leer."}
            ],
            max_tokens=10
        )
        
        print_status("Conexión exitosa con OpenAI API", 'ok')
        print(f"   💬 Respuesta: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print_status(f"Error al conectar con OpenAI: {e}", 'error')
        return False

def print_summary(results):
    """Imprime resumen de resultados"""
    print("\n" + "="*60)
    print("📊 RESUMEN DE VERIFICACIÓN")
    print("="*60)
    
    total = len(results)
    passed = sum(results.values())
    
    for check, status in results.items():
        symbol = '✅' if status else '❌'
        print(f"{symbol} {check}")
    
    print("="*60)
    print(f"Resultado: {passed}/{total} verificaciones exitosas")
    
    if passed == total:
        print("\n🎉 ¡Todo configurado correctamente!")
        print("\n🚀 Puedes iniciar el chatbot:")
        print("   1. python manage.py runserver")
        print("   2. cd frontend && npm run dev")
        print("   3. Ve a http://localhost:5173/chat")
    else:
        print("\n⚠️  Hay problemas que necesitan atención.")
        print("\n📖 Consulta CONFIGURACION_CHATBOT.md para más detalles")

def main():
    """Función principal"""
    print("="*60)
    print("🤖 VERIFICADOR DE CONFIGURACIÓN DEL CHATBOT")
    print("="*60)
    
    results = {}
    
    # Ejecutar todas las verificaciones
    results['Archivo .env'] = check_env_file()
    results['Paquete openai'] = check_openai_package()
    results['App chatbot'] = check_chatbot_app()
    results['Migraciones'] = check_migrations()
    results['Settings Django'] = check_settings()
    
    # Solo probar conexión si todo lo anterior está ok
    if all(results.values()):
        results['Conexión OpenAI'] = test_openai_connection()
    else:
        print("\n⏭️  Saltando prueba de conexión (configuración incompleta)")
        results['Conexión OpenAI'] = False
    
    # Mostrar resumen
    print_summary(results)
    
    # Código de salida
    sys.exit(0 if all(results.values()) else 1)

if __name__ == '__main__':
    main()
