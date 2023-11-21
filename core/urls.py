from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('addToCart/', views.addToCart, name='addToCart'),
    path('removeFromCart/', views.removeFromCart, name='removeFromCart'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.paymentView, name='payment'),
    path('empty_cart/', views.empty_cart, name='empty_cart'),
]