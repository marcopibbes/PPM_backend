from django.urls import path

from . import views

app_name = 'ratingsANDreviews'

urlpatterns = [
    path('rate/<int:receiverId>/', views.rateUser, name='rateUser'),
    path('review/<int:receiverId>/', views.reviewUser, name='reviewUser'),
    path('user/ratings/', views.userRatings, name='userRatings'),
    # path('user/reviews/', views.userReviews, name='userReviews'),
    path('user/reviews/<int:receiverId>/', views.userReviews, name='userReviews'),
    path('myRatingsAndMyReviews/', views.myRatingsAndMyReviews, name='myRatingsAndMyReviews'),
]