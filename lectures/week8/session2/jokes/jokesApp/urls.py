from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard),
    path('jokeAPI/', views.jokAPI),
    path('createJoke/', views.createJoke),
    path('users/', views.allUsers),
    path('user/<int:user_id>/view/', views.otherUser)
]