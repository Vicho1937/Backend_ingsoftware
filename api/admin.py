from django.contrib import admin
from .models import Category, LocalRoute, Review, Favorite

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'created_at']
    search_fields = ['name', 'description']

@admin.register(LocalRoute)
class LocalRouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'address', 'rating', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'description', 'address']
    readonly_fields = ['rating', 'created_at', 'updated_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['route', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['route__name', 'user__username', 'comment']

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'route', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'route__name']
