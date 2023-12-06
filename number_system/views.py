import json
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BaseConversionForm, BaseCalculatorForm, AnswerSubmissionForm, UserForm, ProfileForm
from random import choice, randint
from api.models import Question
from api.serializers import QuestionSerializer
from django.contrib import messages
from .utils.RecursiveFunction import solve2, solve1
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.mail import send_mail, EmailMessage
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView
from .forms import UserRegisterForm, UserPasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, SolverProfile
from django.conf import settings
from number_system.utils import NumberSystem
from number_system.utils import QuestionGenerateorAI
from number_system.utils import ACSLQuestionSolver
from number_system.utils import PCSolver


@csrf_exempt
def index(request):
    return render(request, 'base.html')


@csrf_exempt
def homepage(request):
    return render(request, 'pages/homepage.html')


@csrf_exempt
def base_converter(request):
    if request.method == 'POST':
        form = BaseConversionForm(request.POST)
        if form.is_valid():
            source_base = form.cleaned_data['source_base']
            target_base = form.cleaned_data['target_base']
            input_number = form.cleaned_data['input_number']

            try:
                result_number = NumberSystem.convert_base(source_base, target_base, input_number)
                messages.success(request, f"Conversion result: {result_number}")
            except ValueError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Invalid input. Please check your values.")
    else:
        form = BaseConversionForm()

    return render(request, 'pages/contest1/base_converter.html', {'form': form})


@csrf_exempt
def base_calculator(request):
    result_number = None

    if request.method == 'POST':
        form = BaseCalculatorForm(request.POST)
        if form.is_valid():
            target_base = form.cleaned_data['target_base']
            input_expression = form.cleaned_data['input_expression']
            try:
                result_number = NumberSystem.evaluate_expression(input_expression, target_base)
                messages.success(request, f"Conversion result: {result_number}")
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = BaseCalculatorForm()

    return render(request, 'pages/contest1/base_calculator.html', {'form': form, 'result_number': result_number})


@csrf_exempt
def question_generator_homepage(request):
    return render(request, 'pages/question_generator/question_generator_homepage.html')


def question_generator(request, question_type):
    user_answer = ""
    if request.method == 'POST':
        user = request.user
        if user.is_authenticated:
            solver_profile = SolverProfile.objects.get(user=user)
            question_id = request.session['question']['id']
            question = Question.objects.get(id=question_id)
            solver_profile.questions_solved.add(question)
            solver_profile.save()
        form = AnswerSubmissionForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer']
            question = request.session['question']
            correct = (str(user_answer) == question['answer'].strip().lower())
        else:
            user_answer = ''
            question = ''
            correct = False
    else:
        if randint(0, 1) == 0:
            question = Question.objects.filter(type=question_type)
            if question.exists():
                question = choice(question)
                question = QuestionSerializer(question, many=False).data
            else:
                question = None

        else:
            if question_type == "Computer_Number_Systems":
                question = NumberSystem.generate_question()  # Replace with your data source
                question['id'] = -1
                question['likes'] = 0
            else:
                question = Question.objects.filter(type=question_type)
                if question.exists():
                    question = choice(question)
                    question = QuestionSerializer(question, many=False).data
                else:
                    question = None

        request.session['question'] = question
        form = AnswerSubmissionForm()
        correct = False

    context = {
        'form': form,
        'question': question,
        'finished': request.method == 'POST',
        'correct': correct,
        'user_answer': user_answer,
        'type': question_type,
    }
    return render(request, 'pages/question_generator/question_generator.html', context)


@csrf_exempt
def recursion_solver(request):
    return render(request, 'pages/contest1/recursive_solver.html')


def solve_recursion(request):
    data = json.loads(request.body)
    equations = data['equations']
    conditions = data['conditions']
    value = data['value']
    # if len(value) == 1:
    #     value = value[0]
    # else:
    #     value = value[0] + ',' + value[1]
    # str = RecursiveFunctionAI.recursive_function_solver(equations, conditions, value)
    # return JsonResponse({'result': str})
    if len(value) == 1:
        result = solve1(equations, conditions, int(value[0]))
    else:
        result = solve2(equations, conditions, int(value[0]), int(value[1]))

    if result == "Error":
        return JsonResponse({'result': 'Error'})
    else:
        return JsonResponse({'result': str(result)})


@csrf_exempt
def ide(request):
    return render(request, 'pages/contest1/IDE.html')


@csrf_exempt
def problem_solver(request):
    return render(request, 'pages/premium/question_solver.html')


def like(request, pk):
    question = Question.objects.get(id=pk)
    question.likes = question.likes + 1
    question.save()
    response_data = {'status': 'success', 'message': 'Object updated successfully'}
    return JsonResponse(response_data)


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        Profile.objects.create(user=user)
        SolverProfile.objects.create(user=user)
        # current_site = get_current_site(self.request)
        # mail_subject = 'Activate your account.'
        # message = render_to_string('custom_regloginapp/activation_email.html', {
        #     'user': user,
        #     'domain': current_site.domain,
        #     'token': user.email_token,
        # })
        # to_email = form.cleaned_data.get('email')
        # email = EmailMessage("Hi", "hi welcome to ACSL Guide", to=[to_email])
        # email.send()
        # send_mail(
        #     'Welcome to our site',
        #     'Hello, thank you for registering on our site.',
        #     settings.EMAIL_HOST_USER,
        #     [user.email],
        #     fail_silently=False,
        # )
        return redirect('homepage')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('homepage')


class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = UserPasswordResetForm
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('login')


def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return redirect('homepage')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redirect to some success page, for example, back to the profile page.
            return redirect('profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'pages/user/edit_profile.html', context)


@login_required
def view_profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'pages/user/profile.html', {'profile': user_profile, 'user': request.user})


@staff_member_required(login_url='admin:login')  # Redirect to admin login if not authenticated as staff
def problem_generator(request):
    return render(request, 'pages/admin/generator.html')


def generate_questions(request, question_type):
    data = json.loads(request.body)
    difficulty = data['difficulty']
    result = QuestionGenerateorAI.generate_question(question_type, difficulty)
    return JsonResponse({'question': result})


def test(request):
    return render(request, 'pages/test.html')


def tools(request):
    return render(request, 'pages/tool_box.html')


def view_user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'pages/user/profile.html', {'profile': profile, 'user': user})


def ask_question(request):
    data = json.loads(request.body)
    question = data['question']
    answer = ACSLQuestionSolver.generate_question(question)
    return JsonResponse({'answer': answer})


def ide_run(request):
    data = json.loads(request.body)
    code = data['code']
    language = data['language']
    inputs = data['inputs']
    result = PCSolver.solve(code, inputs)

    return JsonResponse({'output': result})


def solver_profile(request):
    user = request.user
    solver_profile = SolverProfile.objects.get(user=user)
    return render(request, 'pages/user/solver_profile.html', {'solver_profile': solver_profile, 'user': user})


def view_user_solver_profile(request, username):
    user = User.objects.get(username=username)
    solver_profile = SolverProfile.objects.get(user=user)
    return render(request, 'pages/user/solver_profile.html', {'solver_profile': solver_profile, 'user': user})


def view_question(request, pk):
    question = Question.objects.get(id=pk)
    return render(request, 'pages/question_generator/view_question.html', {'question': question})

#changes