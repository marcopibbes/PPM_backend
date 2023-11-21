from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    # The related_name attribute specifies the name of the reverse relation from the Category model back to your model.
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    
    isSold = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    # The related_name attribute specifies the name of the reverse relation from the User model back to your model.
    createdBy = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    