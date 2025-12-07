from django.urls import path
from .views import chat_message, chat_history

urlpatterns = [
    path('message/', chat_message, name='chat_message'),
    path('history/', chat_history, name='chat_history'),
]
