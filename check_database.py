import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruta_local_backend.settings')
django.setup()

from api.models import LocalRoute, Category

print("\n" + "="*50)
print("DIAGNÓSTICO DE BASE DE DATOS")
print("="*50)

total = LocalRoute.objects.count()
print(f"\n📊 Total de lugares en la BD: {total}")

if total > 0:
    print("\n📍 Primeros 10 lugares:")
    for i, lugar in enumerate(LocalRoute.objects.all()[:10], 1):
        print(f"   {i}. {lugar.name} ({lugar.category.name})")
    
    print("\n📁 Lugares por categoría:")
    for cat in Category.objects.all():
        count = LocalRoute.objects.filter(category=cat).count()
        print(f"   {cat.icon} {cat.name}: {count} lugares")
else:
    print("\n⚠️  NO HAY LUGARES EN LA BASE DE DATOS")

print("\n" + "="*50)
