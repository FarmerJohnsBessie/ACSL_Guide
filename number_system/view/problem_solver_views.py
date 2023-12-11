import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from number_system.utils import ACSLQuestionSolver


@csrf_exempt
def problem_solver(request):
    return render(request, 'pages/premium/question_solver.html')


def ask_question(request):
    data = json.loads(request.body)
    question = data['question']
    answer = ACSLQuestionSolver.generate_question(question)
    return JsonResponse({'answer': answer})
