from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Rating, Review

# Create your views here.
@login_required
def rateUser(request, receiverId):
    if request.method == 'POST':
        score = request.POST.get('score')
        receiver = get_object_or_404(User, id=receiverId)
        rating = Rating.objects.create(
            author=request.user,
            receiverId=receiver,
            score=score
        )
        return redirect('ratingsANDreviews:userRatings')
    else:
        return render(request, 'ratingsANDreviews/rating.html', {'receiverId': receiverId})
    
@login_required
def reviewUser(request, receiverId):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            receiver = get_object_or_404(User, id=receiverId)
            review = Review.objects.create(
                author=request.user,
                receiverId=receiver,
                text=text
            )
            return redirect('ratingsANDreviews:userReviews', receiverId=receiverId)
        else:
            return redirect('ratingsANDreviews:userReviews', receiverId=receiverId) 
    else:
        return render(request, 'ratingsANDreviews/review.html', {'receiverId': receiverId})
    
@login_required
def userRatings(request):
    ratings = Rating.objects.filter(author=request.user)
    return render(request, 'ratingsANDreviews/userRatings.html', {'ratings': ratings})

@login_required
def userReviews(request, receiverId):
    reviews = Review.objects.filter(author=request.user)
    return render(request, 'ratingsANDreviews/userReviews.html', {'reviews': reviews})

@login_required
def myRatingsAndMyReviews(request):
    ratings = Rating.objects.filter(author=request.user)
    reviews = Review.objects.filter(author=request.user)
    return render(request, 'ratingsANDreviews/myRatingsAndMyReviews.html', {'ratings': ratings, 'reviews': reviews})
