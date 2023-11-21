from django.db import models
from django.contrib.auth.models import User

from item.models import Item

# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversation' ,on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversation')
    createdAt = models.DateTimeField(auto_now_add=True)
    modfiedAt = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-modfiedAt',)
        
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User, related_name='createdMessages', on_delete=models.CASCADE)