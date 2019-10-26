from django.urls import path

from main import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.registerReviewer),
    path('allcompany/', views.GetAllCompany.as_view()),
    path('allreview/', views.GetAllReviews.as_view())

]