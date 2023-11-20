from django.urls import path
from . import views
from .views import UserRegisterView, UserLoginView, UserPasswordResetView
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

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

    path('problem_solver/', views.problem_solver, name='problem_solver'),

    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', views.logout_user, name='logout'),

    path('accounts/profile/', views.view_profile, name='profile'),
    path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),


]