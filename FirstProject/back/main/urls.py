from django.urls import path

from main import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.registerReviewer),
    path('allReview/', views.GetAllReviews.as_view()),
    path('myReview/', views.GetMyReview.as_view()),
    path('postReview/', views.PostReview.as_view()),
]