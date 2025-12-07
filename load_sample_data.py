"""
Script para cargar datos de ejemplo en la base de datos
Ejecutar con: python load_sample_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ruta_local_backend.settings')
django.setup()

from api.models import Category, LocalRoute
from authentication.models import User

def load_data():
    print("🚀 Cargando datos de ejemplo...")
    
    # Crear categorías
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
    
    print("\n📁 Creando categorías...")
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'icon': cat_data['icon'], 'description': cat_data['description']}
        )
        if created:
            print(f"  ✓ Categoría creada: {category.name}")
        else:
            print(f"  - Categoría ya existe: {category.name}")
    
    # Obtener categorías para asignar a rutas
    restaurantes = Category.objects.get(name='Restaurantes')
    turismo = Category.objects.get(name='Turismo')
    parques = Category.objects.get(name='Parques')
    cafeterias = Category.objects.get(name='Cafeterías')
    museos = Category.objects.get(name='Museos')
    
    # Crear usuario demo si no existe
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
        print("\n👤 Usuario demo creado: demo / demo1234")
    
    # Obtener todas las categorías
    entretenimiento = Category.objects.get(name='Entretenimiento')
    vida_nocturna = Category.objects.get(name='Vida Nocturna')
    compras = Category.objects.get(name='Compras')
    
    # Crear rutas de ejemplo (Santiago, Chile) - Expandidas con más lugares
    routes_data = [
        # MUSEOS
        {
            'name': 'La Chascona',
            'description': 'Casa-museo de Pablo Neruda en el barrio Bellavista. Una de las tres casas del poeta en Chile, con una arquitectura única y objetos personales.',
            'category': museos,
            'address': 'Fernando Márquez de la Plata 0192, Providencia',
            'latitude': -33.4308,
            'longitude': -70.6353,
            'phone': '+56 2 2777 8741',
            'website': 'https://fundacionneruda.org',
            'opening_hours': 'Mar-Dom: 10:00-18:00',
            'image_url': 'https://images.unsplash.com/photo-1568515387631-8b650bbcdb90',
            'rating': 4.7
        },
        {
            'name': 'Museo de la Memoria',
            'description': 'Museo dedicado a las víctimas de violaciones de derechos humanos durante la dictadura militar en Chile (1973-1990).',
            'category': museos,
            'address': 'Matucana 501, Quinta Normal',
            'latitude': -33.4400,
            'longitude': -70.6820,
            'phone': '+56 2 2597 9600',
            'website': 'https://museodelamemoria.cl',
            'opening_hours': 'Mar-Dom: 10:00-18:00',
            'image_url': 'https://images.unsplash.com/photo-1564399579883-451a5d44ec08',
            'rating': 4.8
        },
        {
            'name': 'Museo Nacional de Bellas Artes',
            'description': 'Principal museo de arte de Chile, con colecciones de arte chileno y europeo desde el siglo XVII hasta hoy.',
            'category': museos,
            'address': 'José Miguel de la Barra 650, Parque Forestal',
            'latitude': -33.4353,
            'longitude': -70.6420,
            'phone': '+56 2 2499 1600',
            'website': 'https://www.mnba.gob.cl',
            'opening_hours': 'Mar-Dom: 10:00-18:45',
            'image_url': 'https://images.unsplash.com/photo-1577083552792-a0d461cb1dd6',
            'rating': 4.6
        },
        
        # PARQUES
        {
            'name': 'Cerro San Cristóbal',
            'description': 'El parque urbano más grande de Santiago con vistas panorámicas de 360°. Cuenta con el Santuario de la Inmaculada Concepción, teleférico y funicular.',
            'category': parques,
            'address': 'Pío Nono 450, Recoleta',
            'latitude': -33.4196,
            'longitude': -70.6344,
            'phone': '+56 2 2730 1300',
            'opening_hours': 'Lun-Dom: 08:30-20:00',
            'image_url': 'https://images.unsplash.com/photo-1580671854908-b7cd24de0d27',
            'rating': 4.8
        },
        {
            'name': 'Parque Bicentenario',
            'description': 'Hermoso parque con lagunas artificiales, áreas verdes y esculturas. Perfecto para picnic, deportes al aire libre o simplemente relajarse.',
            'category': parques,
            'address': 'Av. Bicentenario 3800, Vitacura',
            'latitude': -33.3973,
            'longitude': -70.5775,
            'opening_hours': 'Abierto 24 horas',
            'image_url': 'https://images.unsplash.com/photo-1519331379826-f10be5486c6f',
            'rating': 4.7
        },
        {
            'name': 'Parque Forestal',
            'description': 'Parque lineal arbolado junto al río Mapocho, ideal para caminar, hacer ejercicio o pasear en bicicleta. Conecta el barrio Bellas Artes con Lastarria.',
            'category': parques,
            'address': 'Av. Ismael Valdés Vergara, Santiago Centro',
            'latitude': -33.4365,
            'longitude': -70.6425,
            'opening_hours': 'Abierto 24 horas',
            'image_url': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e',
            'rating': 4.5
        },
        
        # RESTAURANTES
        {
            'name': 'Mercado Central',
            'description': 'Mercado histórico famoso por sus mariscos frescos y restaurantes tradicionales. Un ícono arquitectónico de Santiago desde 1872.',
            'category': restaurantes,
            'address': 'San Pablo 967, Santiago Centro',
            'latitude': -33.4370,
            'longitude': -70.6506,
            'phone': '+56 2 2696 8327',
            'website': 'https://mercadocentral.cl',
            'opening_hours': 'Lun-Dom: 06:00-17:00',
            'image_url': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1',
            'rating': 4.4
        },
        {
            'name': 'Boragó',
            'description': 'Restaurante de alta cocina chilena con ingredientes endémicos y silvestres. #38 en The World\'s 50 Best Restaurants 2023.',
            'category': restaurantes,
            'address': 'Av. Nueva Costanera 3467, Vitacura',
            'latitude': -33.4108,
            'longitude': -70.5757,
            'phone': '+56 2 2953 8893',
            'website': 'https://borago.cl',
            'opening_hours': 'Mar-Sáb: 19:00-23:00',
            'image_url': 'https://images.unsplash.com/photo-1414235077428-338989a2e8c0',
            'rating': 4.9
        },
        {
            'name': 'Liguria',
            'description': 'Restaurante tradicional chileno con ambiente bohemio. Famoso por sus chorrillanas, cervezas artesanales y decoración vintage.',
            'category': restaurantes,
            'address': 'Av. Providencia 1373, Providencia',
            'latitude': -33.4289,
            'longitude': -70.6198,
            'phone': '+56 2 2235 7914',
            'opening_hours': 'Lun-Jue: 12:00-01:00, Vie-Sáb: 12:00-02:00',
            'image_url': 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4',
            'rating': 4.5
        },
        
        # CAFETERÍAS
        {
            'name': 'Café Colmado',
            'description': 'Cafetería artesanal con ambiente acogedor y excelente café de especialidad. Ideal para trabajar remoto o reunirse con amigos.',
            'category': cafeterias,
            'address': 'Purísima 257, Recoleta',
            'latitude': -33.4283,
            'longitude': -70.6447,
            'phone': '+56 9 8765 4321',
            'opening_hours': 'Lun-Vie: 08:00-20:00, Sáb-Dom: 09:00-21:00',
            'image_url': 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb',
            'rating': 4.6
        },
        {
            'name': 'Café Literario Balmaceda Arte Joven',
            'description': 'Café cultural con exposiciones de arte, libros y eventos. Perfecto para leer, estudiar o asistir a presentaciones.',
            'category': cafeterias,
            'address': 'Av. Libertador Bernardo O\'Higgins 1371',
            'latitude': -33.4456,
            'longitude': -70.6589,
            'phone': '+56 2 2671 3213',
            'opening_hours': 'Lun-Vie: 09:00-21:00, Sáb: 10:00-20:00',
            'image_url': 'https://images.unsplash.com/photo-1554118811-1e0d58224f24',
            'rating': 4.4
        },
        
        # TURISMO
        {
            'name': 'Plaza de Armas',
            'description': 'Corazón histórico de Santiago, rodeada de edificios patrimoniales como la Catedral Metropolitana, el Correo Central y el Museo Histórico Nacional.',
            'category': turismo,
            'address': 'Plaza de Armas, Santiago Centro',
            'latitude': -33.4372,
            'longitude': -70.6506,
            'opening_hours': 'Abierto 24 horas',
            'image_url': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf',
            'rating': 4.6
        },
        {
            'name': 'Palacio de La Moneda',
            'description': 'Palacio presidencial y sede del gobierno de Chile. Ofrece visitas guiadas gratuitas y el Centro Cultural La Moneda en su subterráneo.',
            'category': turismo,
            'address': 'Moneda s/n, Santiago Centro',
            'latitude': -33.4429,
            'longitude': -70.6542,
            'phone': '+56 2 2690 4000',
            'website': 'https://www.gob.cl',
            'opening_hours': 'Visitas: Sáb-Dom 10:00-18:00',
            'image_url': 'https://images.unsplash.com/photo-1563789031959-4c02bcb41319',
            'rating': 4.7
        },
        {
            'name': 'Barrio Lastarria',
            'description': 'Barrio bohemio y cultural con galerías de arte, restaurantes gourmet, tiendas de diseño y arquitectura patrimonial.',
            'category': turismo,
            'address': 'José Victorino Lastarria, Santiago Centro',
            'latitude': -33.4379,
            'longitude': -70.6386,
            'opening_hours': 'Abierto 24 horas',
            'image_url': 'https://images.unsplash.com/photo-1568515387631-8b650bbcdb90',
            'rating': 4.7
        },
        
        # ENTRETENIMIENTO
        {
            'name': 'Cine Hoyts Parque Arauco',
            'description': 'Complejo de cines con tecnología 3D, 4D y salas Premium. Amplia cartelera de estrenos nacionales e internacionales.',
            'category': entretenimiento,
            'address': 'Av. Kennedy 5413, Las Condes',
            'latitude': -33.4117,
            'longitude': -70.5746,
            'phone': '+56 600 600 4698',
            'website': 'https://www.hoyts.cl',
            'opening_hours': 'Lun-Dom: 11:00-23:00',
            'image_url': 'https://images.unsplash.com/photo-1489599849927-2ee91cede3ba',
            'rating': 4.3
        },
        {
            'name': 'Teatro Municipal de Santiago',
            'description': 'Teatro histórico de ópera, ballet y música clásica. Uno de los teatros más importantes de Latinoamérica.',
            'category': entretenimiento,
            'address': 'Agustinas 794, Santiago Centro',
            'latitude': -33.4380,
            'longitude': -70.6502,
            'phone': '+56 2 2463 8888',
            'website': 'https://municipal.cl',
            'opening_hours': 'Según programación',
            'image_url': 'https://images.unsplash.com/photo-1503095396549-807759245b35',
            'rating': 4.8
        },
        
        # VIDA NOCTURNA
        {
            'name': 'Club La Feria',
            'description': 'Discoteca y club nocturno con música electrónica y fiestas temáticas. Ambiente underground y DJ\'s internacionales.',
            'category': vida_nocturna,
            'address': 'Av. Constitución 275, Providencia',
            'latitude': -33.4291,
            'longitude': -70.6276,
            'phone': '+56 9 9876 5432',
            'opening_hours': 'Vie-Sáb: 23:00-06:00',
            'image_url': 'https://images.unsplash.com/photo-1566417713940-fe7c737a9ef2',
            'rating': 4.2
        },
        {
            'name': 'Bar Liguria Bellavista',
            'description': 'Bar tradicional con terraza, ideal para after office. Cervezas artesanales, cócteles y picoteos.',
            'category': vida_nocturna,
            'address': 'Av. Pío Nono 76, Recoleta',
            'latitude': -33.4313,
            'longitude': -70.6380,
            'phone': '+56 2 2777 8532',
            'opening_hours': 'Lun-Jue: 12:00-01:00, Vie-Sáb: 12:00-03:00',
            'image_url': 'https://images.unsplash.com/photo-1572116469696-31de0f17cc34',
            'rating': 4.4
        },
        
        # COMPRAS
        {
            'name': 'Costanera Center',
            'description': 'El centro comercial más grande de Sudamérica con más de 300 tiendas. Incluye el Sky Costanera, mirador más alto de Latinoamérica (300m).',
            'category': compras,
            'address': 'Av. Andrés Bello 2425, Providencia',
            'latitude': -33.4182,
            'longitude': -70.6066,
            'phone': '+56 2 2916 9200',
            'website': 'https://www.costaneracenter.cl',
            'opening_hours': 'Lun-Dom: 10:00-22:00',
            'image_url': 'https://lh3.googleusercontent.com/p/AF1QipNXE8kCvkBFSa5Z6yJg3VqZ7fqZ9fQ3VqZ7fqZ=s1360-w1360-h1020',
            'rating': 4.5
        },
        {
            'name': 'Parque Arauco',
            'description': 'Centro comercial premium con tiendas de lujo, gastronomía internacional y servicios. Ambiente familiar.',
            'category': compras,
            'address': 'Av. Kennedy 5413, Las Condes',
            'latitude': -33.4117,
            'longitude': -70.5746,
            'phone': '+56 2 2299 0650',
            'website': 'https://www.parquearauco.cl',
            'opening_hours': 'Lun-Dom: 10:00-21:00',
            'image_url': 'https://lh3.googleusercontent.com/p/AF1QipP7VqZ7fqZ9fQ3VqZ7fqZ9fQ3VqZ7fqZ9fQ3V=s1360-w1360-h1020',
            'rating': 4.6
        },
        {
            'name': 'Mall Sport',
            'description': 'Centro comercial enfocado en deportes y vida saludable. Tiendas deportivas, gimnasios y restaurantes healthy.',
            'category': compras,
            'address': 'Av. Las Condes 13451, Las Condes',
            'latitude': -33.4067,
            'longitude': -70.5649,
            'phone': '+56 2 2959 9000',
            'website': 'https://www.mallsport.cl',
            'opening_hours': 'Lun-Dom: 10:00-21:00',
            'image_url': 'https://images.unsplash.com/photo-1556742031-c6961e8560b0',
            'rating': 4.4
        },
        
        # MÁS RESTAURANTES
        {
            'name': 'Osaka',
            'description': 'Restaurante de cocina nikkei (fusión peruana-japonesa). Famoso por su sushi y ceviches. Ambiente moderno y elegante.',
            'category': restaurantes,
            'address': 'Av. Nueva Costanera 3467, Vitacura',
            'latitude': -33.4089,
            'longitude': -70.5772,
            'phone': '+56 2 2953 8652',
            'website': 'https://www.osaka.cl',
            'opening_hours': 'Lun-Dom: 13:00-00:00',
            'image_url': 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351',
            'rating': 4.7
        },
        {
            'name': 'Peumayén Ancestral Food',
            'description': 'Cocina ancestral chilena con ingredientes de pueblos originarios. Experiencia gastronómica única y auténtica.',
            'category': restaurantes,
            'address': 'Constitución 136, Bellavista',
            'latitude': -33.4318,
            'longitude': -70.6369,
            'phone': '+56 2 2738 0107',
            'website': 'https://www.peumayen.cl',
            'opening_hours': 'Mar-Sáb: 13:00-23:00, Dom: 13:00-17:00',
            'image_url': 'https://images.unsplash.com/photo-1555244162-803834f70033',
            'rating': 4.8
        },
        {
            'name': 'Galindo',
            'description': 'Picada tradicional chilena con más de 70 años. Famosa por sus cazuelas, pastel de choclo y platos típicos.',
            'category': restaurantes,
            'address': 'Dardignac 0098, Bellavista',
            'latitude': -33.4297,
            'longitude': -70.6358,
            'phone': '+56 2 2777 0116',
            'opening_hours': 'Lun-Dom: 12:30-01:00',
            'image_url': 'https://images.unsplash.com/photo-1504674900247-0877df9cc836',
            'rating': 4.6
        },
        {
            'name': 'Castillo Forestal',
            'description': 'Restaurante en casona patrimonial con vista al Parque Forestal. Cocina chilena contemporánea y carta de vinos.',
            'category': restaurantes,
            'address': 'Merced 298, Lastarria',
            'latitude': -33.4377,
            'longitude': -70.6398,
            'phone': '+56 2 2638 5534',
            'opening_hours': 'Lun-Dom: 12:00-00:00',
            'image_url': 'https://images.unsplash.com/photo-1466978913421-dad2ebd01d17',
            'rating': 4.5
        },
        
        # MÁS CAFETERÍAS
        {
            'name': 'Café Mosqueto',
            'description': 'Café de especialidad con tostado propio. Ambiente hipster, ideal para trabajar remoto. Wifi gratis y enchufes.',
            'category': cafeterias,
            'address': 'Merced 364, Lastarria',
            'latitude': -33.4384,
            'longitude': -70.6389,
            'phone': '+56 2 2633 5670',
            'opening_hours': 'Lun-Vie: 08:00-20:00, Sáb-Dom: 09:00-20:00',
            'image_url': 'https://images.unsplash.com/photo-1442512595331-e89e73853f31',
            'rating': 4.7
        },
        {
            'name': 'Wonderland Café',
            'description': 'Cafetería temática inspirada en Alicia en el País de las Maravillas. Instagram-friendly con decoración única.',
            'category': cafeterias,
            'address': 'Purísima 251, Recoleta',
            'latitude': -33.4286,
            'longitude': -70.6449,
            'phone': '+56 9 7654 3210',
            'opening_hours': 'Lun-Vie: 09:00-20:00, Sáb-Dom: 10:00-21:00',
            'image_url': 'https://images.unsplash.com/photo-1559305616-3ceb0d988371',
            'rating': 4.5
        },
        {
            'name': 'The Singular Café',
            'description': 'Café boutique en el barrio Lastarria. Pasteles artesanales, café premium y brunches los fines de semana.',
            'category': cafeterias,
            'address': 'Merced 294, Lastarria',
            'latitude': -33.4376,
            'longitude': -70.6399,
            'phone': '+56 2 2940 2900',
            'opening_hours': 'Lun-Dom: 08:00-22:00',
            'image_url': 'https://images.unsplash.com/photo-1521017432531-fbd92d768814',
            'rating': 4.6
        },
        
        # MÁS MUSEOS
        {
            'name': 'Museo Chileno de Arte Precolombino',
            'description': 'Colección de arte precolombino de Mesoamérica, Intermedia, Andes Centrales y Surandinos. Arquitectura colonial.',
            'category': museos,
            'address': 'Bandera 361, Santiago Centro',
            'latitude': -33.4386,
            'longitude': -70.6501,
            'phone': '+56 2 2928 1500',
            'website': 'https://www.museoprecolombino.cl',
            'opening_hours': 'Mar-Dom: 10:00-18:00',
            'image_url': 'https://images.unsplash.com/photo-1595433707802-6b2626ef1c91',
            'rating': 4.7
        },
        {
            'name': 'Centro Cultural Gabriela Mistral (GAM)',
            'description': 'Centro cultural con teatro, exposiciones, talleres y eventos. Arquitectura brutalista emblemática de Santiago.',
            'category': museos,
            'address': 'Av. Libertador Bernardo O\'Higgins 227',
            'latitude': -33.4418,
            'longitude': -70.6424,
            'phone': '+56 2 2566 5500',
            'website': 'https://www.gam.cl',
            'opening_hours': 'Mar-Sáb: 10:00-21:00, Dom: 11:00-19:00',
            'image_url': 'https://images.unsplash.com/photo-1578926314433-e2789279f4aa',
            'rating': 4.6
        },
        
        # MÁS PARQUES
        {
            'name': 'Parque Quinta Normal',
            'description': 'Parque histórico con lagos, museos y áreas verdes. Ideal para familias, picnics y paseos en bote.',
            'category': parques,
            'address': 'Av. Matucana 520, Quinta Normal',
            'latitude': -33.4443,
            'longitude': -70.6782,
            'opening_hours': 'Abierto 24 horas',
            'image_url': 'https://images.unsplash.com/photo-1519331379826-f10be5486c6f',
            'rating': 4.5
        },
        {
            'name': 'Cerro Santa Lucía',
            'description': 'Cerro urbano con jardines, terrazas y miradores. Vista panorámica de Santiago y arquitectura neoclásica.',
            'category': parques,
            'address': 'Santa Lucía, Santiago Centro',
            'latitude': -33.4390,
            'longitude': -70.6435,
            'opening_hours': 'Mar-Dom: 09:00-20:00',
            'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4',
            'rating': 4.6
        },
        {
            'name': 'Parque Araucano',
            'description': 'Parque moderno con áreas deportivas, ciclovías y jardines temáticos. Conectado con Parque Arauco.',
            'category': parques,
            'address': 'Av. Presidente Riesco 5330, Las Condes',
            'latitude': -33.4114,
            'longitude': -70.5774,
            'opening_hours': 'Abierto 24 horas',
            'image_url': 'https://images.unsplash.com/photo-1587502537147-2ba64a117f59',
            'rating': 4.7
        },
        
        # MÁS TURISMO
        {
            'name': 'Barrio Bellavista',
            'description': 'Barrio bohemio con galerías de arte, restaurantes, bares y vida nocturna. Murales coloridos y ambiente artístico.',
            'category': turismo,
            'address': 'Bellavista, Recoleta',
            'latitude': -33.4312,
            'longitude': -70.6371,
            'opening_hours': 'Abierto 24 horas',
            'image_url': 'https://images.unsplash.com/photo-1524659467832-5b91f36f9676',
            'rating': 4.5
        },
        {
            'name': 'Mercado La Vega',
            'description': 'Mercado popular con frutas, verduras y comida típica chilena. Auténtica experiencia local y precios económicos.',
            'category': turismo,
            'address': 'Antonia López de Bello 750, Recoleta',
            'latitude': -33.4248,
            'longitude': -70.6438,
            'opening_hours': 'Lun-Dom: 08:00-18:00',
            'image_url': 'https://images.unsplash.com/photo-1488459716781-31db52582fe9',
            'rating': 4.4
        },
        {
            'name': 'Patio Bellavista',
            'description': 'Centro comercial al aire libre con restaurantes, bares y tiendas de artesanía. Arquitectura colorida y eventos en vivo.',
            'category': turismo,
            'address': 'Constitución 30, Bellavista',
            'latitude': -33.4315,
            'longitude': -70.6362,
            'phone': '+56 2 2732 7600',
            'website': 'https://www.patiobellavista.cl',
            'opening_hours': 'Lun-Dom: 10:00-23:00',
            'image_url': 'https://images.unsplash.com/photo-1555400589-e8507ba82d50',
            'rating': 4.3
        },
        
        # MÁS ENTRETENIMIENTO
        {
            'name': 'Fantasilandia',
            'description': 'Parque de diversiones más grande de Chile con montañas rusas, juegos mecánicos y shows en vivo.',
            'category': entretenimiento,
            'address': 'Av. Beauchef 938, Parque O\'Higgins',
            'latitude': -33.4629,
            'longitude': -70.6732,
            'phone': '+56 2 2476 8600',
            'website': 'https://www.fantasilandia.cl',
            'opening_hours': 'Según temporada',
            'image_url': 'https://images.unsplash.com/photo-1524850011238-e3d235c7d4c9',
            'rating': 4.5
        },
        {
            'name': 'Centro Cultural Estación Mapocho',
            'description': 'Antigua estación de trenes convertida en centro cultural. Exposiciones, ferias y eventos de gran escala.',
            'category': entretenimiento,
            'address': 'Plaza de la Cultura s/n, Santiago Centro',
            'latitude': -33.4289,
            'longitude': -70.6533,
            'phone': '+56 2 2787 0000',
            'website': 'https://www.estacionmapocho.cl',
            'opening_hours': 'Según eventos',
            'image_url': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64',
            'rating': 4.6
        },
        {
            'name': 'Movistar Arena',
            'description': 'Arena multiuso para conciertos, eventos deportivos y espectáculos internacionales. Capacidad 15,000 personas.',
            'category': entretenimiento,
            'address': 'Av. Beauchef 1204, Parque O\'Higgins',
            'latitude': -33.4619,
            'longitude': -70.6722,
            'phone': '+56 2 2977 4000',
            'website': 'https://www.movistar-arena.cl',
            'opening_hours': 'Según eventos',
            'image_url': 'https://images.unsplash.com/photo-1501281668745-f7f57925c3b4',
            'rating': 4.4
        },
        
        # MÁS VIDA NOCTURNA
        {
            'name': 'Club La Batuta',
            'description': 'Club underground con música electrónica y techno. DJs locales e internacionales, ambiente alternativo.',
            'category': vida_nocturna,
            'address': 'Loreto 33, Bellavista',
            'latitude': -33.4304,
            'longitude': -70.6362,
            'opening_hours': 'Vie-Sáb: 23:30-06:00',
            'image_url': 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819',
            'rating': 4.3
        },
        {
            'name': 'The Clinic Bar',
            'description': 'Bar temático inspirado en la revista The Clinic. Karaoke, música en vivo y ambiente relajado.',
            'category': vida_nocturna,
            'address': 'Monjitas 578, Santiago Centro',
            'latitude': -33.4385,
            'longitude': -70.6465,
            'phone': '+56 2 2639 9693',
            'opening_hours': 'Lun-Sáb: 18:00-03:00',
            'image_url': 'https://images.unsplash.com/photo-1514933651103-005eec06c04b',
            'rating': 4.2
        },
        {
            'name': 'Bar The Monkey House',
            'description': 'Cocktail bar con mixología premium. Cócteles autorales, ambiente íntimo y música jazz en vivo.',
            'category': vida_nocturna,
            'address': 'General Holley 171, Providencia',
            'latitude': -33.4274,
            'longitude': -70.6145,
            'phone': '+56 2 2235 7901',
            'opening_hours': 'Mar-Sáb: 19:00-02:00',
            'image_url': 'https://images.unsplash.com/photo-1470337458703-46ad1756a187',
            'rating': 4.7
        },
    ]
    
    print("\n📍 Creando rutas de ejemplo...")
    for route_data in routes_data:
        route, created = LocalRoute.objects.get_or_create(
            name=route_data['name'],
            defaults={**route_data, 'created_by': demo_user}
        )
        if created:
            print(f"  ✓ Ruta creada: {route.name}")
        else:
            print(f"  - Ruta ya existe: {route.name}")
    
    print("\n✅ Datos de ejemplo cargados exitosamente!")
    print(f"\n📊 Resumen:")
    print(f"   Categorías: {Category.objects.count()}")
    print(f"   Rutas: {LocalRoute.objects.count()}")
    print(f"   Usuarios: {User.objects.count()}")
    print("\n🎉 ¡Listo! Puedes iniciar el servidor y explorar la aplicación.")

if __name__ == '__main__':
    load_data()
