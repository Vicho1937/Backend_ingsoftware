import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruta_local_backend.settings')
django.setup()

from api.models import Category, LocalRoute, Review, Favorite

print("🗑️  Eliminando datos antiguos...")
Review.objects.all().delete()
Favorite.objects.all().delete()
LocalRoute.objects.all().delete()
Category.objects.all().delete()
print("✅ Datos eliminados!")
