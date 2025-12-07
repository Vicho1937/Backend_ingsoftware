"""
Script para FORZAR la carga de TODOS los lugares
Ejecutar con: python force_reload_all.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruta_local_backend.settings')
django.setup()

from api.models import Category, LocalRoute, Review, Favorite
from authentication.models import User

print("🗑️  PASO 1: Limpiando base de datos...")
Review.objects.all().delete()
Favorite.objects.all().delete()
LocalRoute.objects.all().delete()
Category.objects.all().delete()
User.objects.filter(is_superuser=False).delete()
print("✅ Base de datos limpia\n")

print("📁 PASO 2: Creando categorías...")
categories_data = [
    {'name': 'Restaurantes', 'icon': '🍽️', 'description': 'Los mejores lugares para comer'},
    {'name': 'Turismo', 'icon': '🏛️', 'description': 'Lugares turísticos y atracciones'},
    {'name': 'Entretenimiento', 'icon': '🎭', 'description': 'Cines, teatros y más'},
    {'name': 'Parques', 'icon': '🌳', 'description': 'Espacios verdes y recreativos'},
    {'name': 'Museos', 'icon': '🖼️', 'description': 'Arte y cultura'},
    {'name': 'Cafeterías', 'icon': '☕', 'description': 'Café y lugares acogedores'},
    {'name': 'Vida Nocturna', 'icon': '🌙', 'description': 'Bares y clubes'},
    {'name': 'Compras', 'icon': '🛍️', 'description': 'Centros comerciales y tiendas'},
]

for cat_data in categories_data:
    Category.objects.create(**cat_data)
    print(f"  ✓ {cat_data['name']}")

print(f"\n✅ {Category.objects.count()} categorías creadas\n")

print("👤 PASO 3: Creando usuario demo...")
demo_user, created = User.objects.get_or_create(
    username='demo',
    defaults={
        'email': 'demo@rutalocal.com',
        'first_name': 'Usuario',
        'last_name': 'Demo',
        'role': 'user'
    }
)
if created:
    demo_user.set_password('demo1234')
    demo_user.save()
print("✅ Usuario demo listo\n")

print("📍 PASO 4: Creando 42 LUGARES...")

# Obtener categorías
restaurantes = Category.objects.get(name='Restaurantes')
turismo = Category.objects.get(name='Turismo')
entretenimiento = Category.objects.get(name='Entretenimiento')
parques = Category.objects.get(name='Parques')
museos = Category.objects.get(name='Museos')
cafeterias = Category.objects.get(name='Cafeterías')
vida_nocturna = Category.objects.get(name='Vida Nocturna')
compras = Category.objects.get(name='Compras')

lugares = [
    # MUSEOS (5)
    {'name': 'La Chascona', 'category': museos, 'address': 'Fernando Márquez de la Plata 0192', 'latitude': -33.4308, 'longitude': -70.6353, 'description': 'Casa-museo de Pablo Neruda', 'image_url': 'https://images.unsplash.com/photo-1568515387631-8b650bbcdb90'},
    {'name': 'Museo de la Memoria', 'category': museos, 'address': 'Matucana 501', 'latitude': -33.4400, 'longitude': -70.6820, 'description': 'Museo de derechos humanos', 'image_url': 'https://images.unsplash.com/photo-1564399579883-451a5d44ec08'},
    {'name': 'Museo Bellas Artes', 'category': museos, 'address': 'José Miguel de la Barra 650', 'latitude': -33.4353, 'longitude': -70.6420, 'description': 'Arte chileno y europeo', 'image_url': 'https://images.unsplash.com/photo-1577083552792-a0d461cb1dd6'},
    {'name': 'Museo Precolombino', 'category': museos, 'address': 'Bandera 361', 'latitude': -33.4386, 'longitude': -70.6501, 'description': 'Arte precolombino', 'image_url': 'https://images.unsplash.com/photo-1595433707802-6b2626ef1c91'},
    {'name': 'Centro Cultural GAM', 'category': museos, 'address': 'Av. Libertador B. O\'Higgins 227', 'latitude': -33.4418, 'longitude': -70.6424, 'description': 'Centro cultural', 'image_url': 'https://images.unsplash.com/photo-1578926314433-e2789279f4aa'},
    
    # PARQUES (6)
    {'name': 'Cerro San Cristóbal', 'category': parques, 'address': 'Pío Nono 450', 'latitude': -33.4196, 'longitude': -70.6344, 'description': 'Parque urbano más grande', 'image_url': 'https://images.unsplash.com/photo-1580671854908-b7cd24de0d27'},
    {'name': 'Parque Bicentenario', 'category': parques, 'address': 'Av. Bicentenario 3800', 'latitude': -33.3973, 'longitude': -70.5775, 'description': 'Parque con lagunas', 'image_url': 'https://images.unsplash.com/photo-1519331379826-f10be5486c6f'},
    {'name': 'Parque Forestal', 'category': parques, 'address': 'Av. Ismael Valdés Vergara', 'latitude': -33.4365, 'longitude': -70.6425, 'description': 'Parque lineal arbolado', 'image_url': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e'},
    {'name': 'Parque Quinta Normal', 'category': parques, 'address': 'Av. Matucana 520', 'latitude': -33.4443, 'longitude': -70.6782, 'description': 'Parque histórico con lagos', 'image_url': 'https://images.unsplash.com/photo-1519331379826-f10be5486c6f'},
    {'name': 'Cerro Santa Lucía', 'category': parques, 'address': 'Santa Lucía', 'latitude': -33.4390, 'longitude': -70.6435, 'description': 'Cerro urbano con jardines', 'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4'},
    {'name': 'Parque Araucano', 'category': parques, 'address': 'Av. Presidente Riesco 5330', 'latitude': -33.4114, 'longitude': -70.5774, 'description': 'Parque moderno deportivo', 'image_url': 'https://images.unsplash.com/photo-1587502537147-2ba64a117f59'},
    
    # RESTAURANTES (7)
    {'name': 'Mercado Central', 'category': restaurantes, 'address': 'San Pablo 967', 'latitude': -33.4370, 'longitude': -70.6506, 'description': 'Mariscos frescos', 'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1'},
    {'name': 'Boragó', 'category': restaurantes, 'address': 'Av. Nueva Costanera 3467', 'latitude': -33.4108, 'longitude': -70.5757, 'description': 'Alta cocina chilena', 'image_url': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0'},
    {'name': 'Liguria', 'category': restaurantes, 'address': 'Av. Providencia 1373', 'latitude': -33.4289, 'longitude': -70.6198, 'description': 'Restaurante tradicional', 'image_url': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4'},
    {'name': 'Osaka', 'category': restaurantes, 'address': 'Av. Nueva Costanera 3467', 'latitude': -33.4089, 'longitude': -70.5772, 'description': 'Cocina nikkei', 'image_url': 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351'},
    {'name': 'Peumayén', 'category': restaurantes, 'address': 'Constitución 136', 'latitude': -33.4318, 'longitude': -70.6369, 'description': 'Cocina ancestral chilena', 'image_url': 'https://images.unsplash.com/photo-1555244162-803834f70033'},
    {'name': 'Galindo', 'category': restaurantes, 'address': 'Dardignac 0098', 'latitude': -33.4297, 'longitude': -70.6358, 'description': 'Picada tradicional', 'image_url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836'},
    {'name': 'Castillo Forestal', 'category': restaurantes, 'address': 'Merced 298', 'latitude': -33.4377, 'longitude': -70.6398, 'description': 'Casona patrimonial', 'image_url': 'https://images.unsplash.com/photo-1466978913421-dad2ebd01d17'},
    
    # CAFETERÍAS (5)
    {'name': 'Café Colmado', 'category': cafeterias, 'address': 'Purísima 257', 'latitude': -33.4283, 'longitude': -70.6447, 'description': 'Café de especialidad', 'image_url': 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb'},
    {'name': 'Café Literario Balmaceda', 'category': cafeterias, 'address': 'Av. Libertador B. O\'Higgins 1371', 'latitude': -33.4456, 'longitude': -70.6589, 'description': 'Café cultural', 'image_url': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24'},
    {'name': 'Café Mosqueto', 'category': cafeterias, 'address': 'Merced 364', 'latitude': -33.4384, 'longitude': -70.6389, 'description': 'Tostado propio', 'image_url': 'https://images.unsplash.com/photo-1442512595331-e89e73853f31'},
    {'name': 'Wonderland Café', 'category': cafeterias, 'address': 'Purísima 251', 'latitude': -33.4286, 'longitude': -70.6449, 'description': 'Temático Alicia', 'image_url': 'https://images.unsplash.com/photo-1559305616-3ceb0d988371'},
    {'name': 'The Singular Café', 'category': cafeterias, 'address': 'Merced 294', 'latitude': -33.4376, 'longitude': -70.6399, 'description': 'Café boutique', 'image_url': 'https://images.unsplash.com/photo-1521017432531-fbd92d768814'},
    
    # TURISMO (6)
    {'name': 'Plaza de Armas', 'category': turismo, 'address': 'Plaza de Armas', 'latitude': -33.4372, 'longitude': -70.6506, 'description': 'Centro histórico', 'image_url': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf'},
    {'name': 'Palacio La Moneda', 'category': turismo, 'address': 'Moneda s/n', 'latitude': -33.4429, 'longitude': -70.6542, 'description': 'Palacio presidencial', 'image_url': 'https://images.unsplash.com/photo-1563789031959-4c02bcb41319'},
    {'name': 'Barrio Lastarria', 'category': turismo, 'address': 'José Victorino Lastarria', 'latitude': -33.4379, 'longitude': -70.6386, 'description': 'Barrio bohemio', 'image_url': 'https://images.unsplash.com/photo-1568515387631-8b650bbcdb90'},
    {'name': 'Barrio Bellavista', 'category': turismo, 'address': 'Bellavista', 'latitude': -33.4312, 'longitude': -70.6371, 'description': 'Arte y galerías', 'image_url': 'https://images.unsplash.com/photo-1524659467832-5b91f36f9676'},
    {'name': 'Mercado La Vega', 'category': turismo, 'address': 'Antonia López de Bello 750', 'latitude': -33.4248, 'longitude': -70.6438, 'description': 'Mercado popular', 'image_url': 'https://images.unsplash.com/photo-1488459716781-31db52582fe9'},
    {'name': 'Patio Bellavista', 'category': turismo, 'address': 'Constitución 30', 'latitude': -33.4315, 'longitude': -70.6362, 'description': 'Centro comercial abierto', 'image_url': 'https://images.unsplash.com/photo-1555400589-e8507ba82d50'},
    
    # ENTRETENIMIENTO (5)
    {'name': 'Cine Hoyts Parque Arauco', 'category': entretenimiento, 'address': 'Av. Kennedy 5413', 'latitude': -33.4117, 'longitude': -70.5746, 'description': 'Complejo de cines', 'image_url': 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba'},
    {'name': 'Teatro Municipal', 'category': entretenimiento, 'address': 'Agustinas 794', 'latitude': -33.4380, 'longitude': -70.6502, 'description': 'Teatro de ópera', 'image_url': 'https://images.unsplash.com/photo-1503095396549-807759245b35'},
    {'name': 'Fantasilandia', 'category': entretenimiento, 'address': 'Av. Beauchef 938', 'latitude': -33.4629, 'longitude': -70.6732, 'description': 'Parque de diversiones', 'image_url': 'https://images.unsplash.com/photo-1524850011238-e3d235c7d4c9'},
    {'name': 'Estación Mapocho', 'category': entretenimiento, 'address': 'Plaza de la Cultura s/n', 'latitude': -33.4289, 'longitude': -70.6533, 'description': 'Centro cultural', 'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64'},
    {'name': 'Movistar Arena', 'category': entretenimiento, 'address': 'Av. Beauchef 1204', 'latitude': -33.4619, 'longitude': -70.6722, 'description': 'Arena de conciertos', 'image_url': 'https://images.unsplash.com/photo-1501281668745-f7f57925c3b4'},
    
    # VIDA NOCTURNA (5)
    {'name': 'Club La Feria', 'category': vida_nocturna, 'address': 'Av. Constitución 275', 'latitude': -33.4291, 'longitude': -70.6276, 'description': 'Discoteca electrónica', 'image_url': 'https://images.unsplash.com/photo-1566417713940-fe7c737a9ef2'},
    {'name': 'Bar Liguria Bellavista', 'category': vida_nocturna, 'address': 'Av. Pío Nono 76', 'latitude': -33.4313, 'longitude': -70.6380, 'description': 'Bar con terraza', 'image_url': 'https://images.unsplash.com/photo-1572116469696-31de0f17cc34'},
    {'name': 'Club La Batuta', 'category': vida_nocturna, 'address': 'Loreto 33', 'latitude': -33.4304, 'longitude': -70.6362, 'description': 'Club underground', 'image_url': 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819'},
    {'name': 'The Clinic Bar', 'category': vida_nocturna, 'address': 'Monjitas 578', 'latitude': -33.4385, 'longitude': -70.6465, 'description': 'Bar temático', 'image_url': 'https://images.unsplash.com/photo-1514933651103-005eec06c04b'},
    {'name': 'The Monkey House', 'category': vida_nocturna, 'address': 'General Holley 171', 'latitude': -33.4274, 'longitude': -70.6145, 'description': 'Cocktail bar', 'image_url': 'https://images.unsplash.com/photo-1470337458703-46ad1756a187'},
    
    # COMPRAS (3)
    {'name': 'Costanera Center', 'category': compras, 'address': 'Av. Andrés Bello 2425', 'latitude': -33.4182, 'longitude': -70.6066, 'description': 'Mall más grande', 'image_url': 'https://images.unsplash.com/photo-1519567241046-7f570eee3ce6'},
    {'name': 'Parque Arauco', 'category': compras, 'address': 'Av. Kennedy 5413', 'latitude': -33.4117, 'longitude': -70.5746, 'description': 'Mall premium', 'image_url': 'https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a'},
    {'name': 'Mall Sport', 'category': compras, 'address': 'Av. Las Condes 13451', 'latitude': -33.4067, 'longitude': -70.5649, 'description': 'Mall deportivo', 'image_url': 'https://images.unsplash.com/photo-1556742031-c6961e8560b0'},
]

count = 0
for lugar in lugares:
    LocalRoute.objects.create(
        created_by=demo_user,
        rating=4.5,
        **lugar
    )
    count += 1
    print(f"  ✓ {count}. {lugar['name']}")

print(f"\n🎉 ¡COMPLETADO!")
print(f"\n📊 TOTALES:")
print(f"   ✅ Categorías: {Category.objects.count()}")
print(f"   ✅ Lugares: {LocalRoute.objects.count()}")
print(f"   ✅ Usuarios: {User.objects.count()}")
