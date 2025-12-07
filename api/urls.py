from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, LocalRouteViewSet, ReviewViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'routes', LocalRouteViewSet, basename='route')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'favorites', FavoriteViewSet, basename='favorite')

urlpatterns = [
    path('', include(router.urls)),
]
