

from django.db import models
from django.conf import settings

class ChatHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='chat_history')
    session_id = models.CharField(max_length=100)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'chat_history'
        verbose_name = 'Historial de Chat'
        verbose_name_plural = 'Historiales de Chat'
        ordering = ['-created_at']
    
    def __str__(self):
        user_name = self.user.username if self.user else 'Anónimo'
        return f"{user_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
