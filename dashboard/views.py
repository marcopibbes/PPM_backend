from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import Item
from core.models import Cart

# Create your views here.

@login_required
def index(request):
    items = Item.objects.filter(createdBy=request.user)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    
    return render(request, 'dashboard/index.html', {
        'items': items,
        'cart': cart,
    }) 
    

