from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('base_converter/', views.base_converter, name="base_converter")
]