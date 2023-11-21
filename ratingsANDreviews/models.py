from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sentRatings')
    receiverId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiverRatings')
    score = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sentReviews')
    receiverId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiverReviews')
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)