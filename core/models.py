from django.db import models    
from django.contrib.auth.models import User
import uuid

from item.models import Item

# Create your models here.
class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    #Calcola il prezzo totale del carrello, sommando il totale_price di ogni elemento nel carrello
    @property
    def totalPrice(self):
        cartItems = self.cartItems.all()
        total = sum([item.item.price * item.quantity for item in cartItems])
        return total
    
    @property
    def numOfItems(self):
        #Calcola il numero totale di elementi nel carrello
        cartItems = self.cartItems.all()
        quantity = sum([item.quantity for item in cartItems])
        return quantity
    
    
class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='itemsCart')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartItems')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.item.name