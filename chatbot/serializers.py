from rest_framework import serializers
from .models import ChatHistory

class ChatMessageSerializer(serializers.Serializer):
    message = serializers.CharField(required=True)
    session_id = serializers.CharField(required=False)
    location = serializers.DictField(required=False, child=serializers.FloatField())

class ChatHistorySerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = ChatHistory
        fields = ['id', 'user', 'user_name', 'session_id', 'message', 'response', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
