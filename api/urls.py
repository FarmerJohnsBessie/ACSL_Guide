from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="getRoutes"),
    path('questions/create/', views.createQuestion, name="createQuestion"),
    path('questions/<str:pk>/', views.getQuestion, name="getQuestion"),
    path('questions/', views.getQuestions, name="getQuestions"),
]