from rest_framework import serializers
from .models import Category, LocalRoute, Review, Favorite
from authentication.serializers import UserSerializer

class CategorySerializer(serializers.ModelSerializer):
    routes_count = serializers.IntegerField(source='routes.count', read_only=True)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'routes_count', 'created_at']
        read_only_fields = ['id', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True, required=False)
    
    class Meta:
        model = Review
        fields = ['id', 'route', 'user', 'user_id', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'route', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class LocalRouteSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_icon = serializers.CharField(source='category.icon', read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)
    average_rating = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    
    class Meta:
        model = LocalRoute
        fields = [
            'id', 'name', 'description', 'category', 'category_name', 'category_icon', 'address',
            'latitude', 'longitude', 'phone', 'email', 'website', 'opening_hours',
            'rating', 'image_url', 'is_active', 'reviews', 'reviews_count',
            'average_rating', 'is_favorite', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'rating', 'created_at', 'updated_at']
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum([r.rating for r in reviews]) / len(reviews)
        return 0
    
    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Favorite.objects.filter(user=request.user, route=obj).exists()
        return False

class LocalRouteListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_icon = serializers.CharField(source='category.icon', read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)
    average_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = LocalRoute
        fields = [
            'id', 'name', 'description', 'category', 'category_name', 'category_icon', 'address',
            'latitude', 'longitude', 'phone', 'rating', 'image_url', 'reviews_count', 'average_rating', 'created_at'
        ]
    
    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews:
            return sum([r.rating for r in reviews]) / len(reviews)
        return 0

class FavoriteSerializer(serializers.ModelSerializer):
    route = LocalRouteListSerializer(read_only=True)
    route_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Favorite
        fields = ['id', 'route', 'route_id', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
