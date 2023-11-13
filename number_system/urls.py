from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('base_converter/', views.base_converter, name="base_converter"),
    path('base_calculator/', views.base_calculator, name='base_calculator'),

    path('question_generator/', views.question_generator_homepage, name='question_generator_homepage'),
    path('question_generator/<str:question_type>/', views.question_generator, name='question_generator'),

    path('recursion_solver/', views.recursion_solver, name='recursion_solver'),
    path('IDE/', views.ide, name='ide'),

    path('update/like/<str:pk>/', views.like, name="like"),
    path('solve/recursion/', views.solve_recursion, name="solve_recursion"),
]