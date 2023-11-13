import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import BaseConversionForm, BaseCalculatorForm, AnswerSubmissionForm
from random import choice
from api.models import Question
from api.serializers import QuestionSerializer
from number_system.utils.NumberSystem import *
from number_system.utils.RecursiveFunction import *
from django.contrib import messages


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
                result_number = convert_base(source_base, target_base, input_number)
                messages.success(request, f"Conversion result: {result_number}")
            except ValueError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Invalid input. Please check your values.")
    else:
        form = BaseConversionForm()

    return render(request, 'pages/base_converter.html', {'form': form})


@csrf_exempt
def base_calculator(request):
    result_number = None

    if request.method == 'POST':
        form = BaseCalculatorForm(request.POST)
        if form.is_valid():
            target_base = form.cleaned_data['target_base']
            input_expression = form.cleaned_data['input_expression']
            try:
                result_number = evaluate_expression(input_expression, target_base)
                messages.success(request, f"Conversion result: {result_number}")
            except ValueError as e:
                messages.error(request, str(e))
    else:
        form = BaseCalculatorForm()

    return render(request, 'pages/base_calculator.html', {'form': form, 'result_number': result_number})


@csrf_exempt
def question_generator_homepage(request):
    return render(request, 'pages/question_generator/question_generator_homepage.html')

def question_generator(request, question_type):
    user_answer = ""
    if request.method == 'POST':
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
                question = generate_question()  # Replace with your data source
                question['id'] = -1
                question['likes'] = 0
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
    return render(request, 'pages/contest2/recursive_solver.html')


def solve_recursion(request):
    data = json.loads(request.body)
    equations = data['equations']
    conditions = data['conditions']
    value = data['value']

    if len(value) == 1:
        result = f(int(value[0]), equations, conditions)
    else:
        result = recursive_function({'x': int(value[0]), 'y': int(value[1])}, equations, conditions)

    if result == "Error":
        return JsonResponse({'result': 'Error'})
    else:
        return JsonResponse({'result': str(result)})


@csrf_exempt
def ide(request):
    return render(request, 'pages/contest3/ide.html')


def like(request, pk):
    question = Question.objects.get(id=pk)
    question.likes = question.likes + 1
    question.save()
    response_data = {'status': 'success', 'message': 'Object updated successfully'}
    return JsonResponse(response_data)
