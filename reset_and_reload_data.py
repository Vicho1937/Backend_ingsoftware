"""
Script para ELIMINAR todos los datos y recargar los nuevos
Ejecutar con: python reset_and_reload_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruta_local_backend.settings')
django.setup()

from api.models import Category, LocalRoute, Review, Favorite
from authentication.models import User

def reset_and_reload():
    print("🗑️  ELIMINANDO DATOS ANTIGUOS...")
    
    # Eliminar en orden correcto (respetando foreign keys)
    print("  - Eliminando reseñas...")
    Review.objects.all().delete()
    
    print("  - Eliminando favoritos...")
    Favorite.objects.all().delete()
    
    print("  - Eliminando rutas...")
    LocalRoute.objects.all().delete()
    
    print("  - Eliminando categorías...")
    Category.objects.all().delete()
    
    print("  - Eliminando usuarios (excepto superusuarios)...")
    User.objects.filter(is_superuser=False).delete()
    
    print("\n✅ Datos antiguos eliminados correctamente!\n")
    
    # Ahora cargar los nuevos datos
    print("🚀 CARGANDO DATOS NUEVOS...")
    
    # Importar y ejecutar el script de carga
    import load_sample_data
    load_sample_data.load_data()

if __name__ == '__main__':
    confirm = input("⚠️  ESTO ELIMINARÁ TODOS LOS DATOS. ¿Continuar? (si/no): ")
    if confirm.lower() in ['si', 's', 'yes', 'y']:
        reset_and_reload()
    else:
        print("❌ Operación cancelada")
