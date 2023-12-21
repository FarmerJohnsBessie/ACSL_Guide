from django.urls import path
from number_system.view import user_views, admin_views, toolbox_views, question_generator_views, extra_views, \
    problem_solver_views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [

    path('', extra_views.homepage, name='homepage'),
    path('test/', extra_views.test, name='test'),
    # =============== Tool Box Views ===============
    path('tools/', toolbox_views.tools, name='tools'),
    path('base_converter/', toolbox_views.base_converter, name="base_converter"),
    path('base_calculator/', toolbox_views.base_calculator, name='base_calculator'),
    path('recursion_solver/', toolbox_views.recursion_solver, name='recursion_solver'),
    path('solve/recursion/', toolbox_views.solve_recursion, name="solve_recursion"),
    path('IDE/', toolbox_views.ide, name='ide'),
    path('ide/run/', toolbox_views.ide_run, name='ide_run'),

    # =============== Admin Views ===============
    path('admin-tools/problem-generator/', admin_views.problem_generator, name='admin_problem_generator'),
    path('generate/<str:question_type>/', admin_views.generate_questions, name='generate_question'),

    # =============== Problem Solver Views ===============
    path('problem_solver/', problem_solver_views.problem_solver, name='problem_solver'),
    path('ask-question/', problem_solver_views.ask_question, name='ask_question'),

    # =============== Question Generator Views ===============
    path('question_generator/', question_generator_views.question_generator_homepage,
         name='question_generator_homepage'),
    path('question_generator/<str:question_type>/', question_generator_views.question_generator,
         name='question_generator'),
    path('question/<str:pk>/', question_generator_views.view_question, name='view_question'),
    path('update/like/<str:pk>/', question_generator_views.like, name="like"),

    # =============== User Views ===============
    path('accounts/profile/', user_views.view_profile, name='profile'),
    path('accounts/profile/edit/', user_views.edit_profile, name='edit_profile'),
    path('accounts/profile/solver_profile', user_views.solver_profile, name='solver_profile'),
    path('accounts/profile/users/<str:username>/', user_views.view_user_profile, name='view_profile'),
    path('accounts/profile/users/<str:username>/solver_profile', user_views.view_user_solver_profile,
         name='view_solver_profile'),
    path('register/', user_views.UserRegisterView.as_view(), name='register'),
    path('login/', user_views.UserLoginView.as_view(), name='login'),
    path('reset-password/', user_views.UserPasswordResetView.as_view(), name='reset_password'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', user_views.logout_user, name='logout'),

# some changes in the branch
]
