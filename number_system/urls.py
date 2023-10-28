from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('base_converter/', views.base_converter, name="base_converter"),
    path('base_calculator/', views.base_calculator, name='base_calculator')
]