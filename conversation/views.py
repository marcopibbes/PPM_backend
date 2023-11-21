from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item
from .models import Conversation
from .forms import ConversationMessageForm
from core.models import Cart

# Create your views here.
@login_required
def newConversation(request, itemPk):
    item = get_object_or_404(Item, pk=itemPk)
    
    if item.createdBy == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversations: 
        # if conversation already exists, redirect to conversation
        return redirect('conversation:detail', pk=conversations.first().id)
    
    if request.method  == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.createdBy)
            conversation.save()
            
            conversationMessage = form.save(commit=False)
            conversationMessage.conversation = conversation
            conversationMessage.createdBy = request.user
            conversationMessage.save()
            
            return redirect('item:detail', pk=itemPk)
    else:
        # create new empty form
        form = ConversationMessageForm()
        
    return render(request, 'conversation/new.html', {
        'form': form,
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'cart': cart,
    })

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    cart = None
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    
    if request.method  == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversationMessage = form.save(commit=False)
            conversationMessage.conversation = conversation
            conversationMessage.createdBy = request.user
            conversationMessage.save()
            
            conversation.save()
            
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
        'cart': cart,
    })