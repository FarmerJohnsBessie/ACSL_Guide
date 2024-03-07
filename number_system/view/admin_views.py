import json
import re

from django.http import JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from number_system.utils import QuestionGeneratorAI


@staff_member_required(login_url='admin:login')  # Redirect to admin login if not authenticated as staff
def problem_generator(request):
    return render(request, 'pages/admin/generator.html')


def generate_questions(request, question_type):
    data = json.loads(request.body)
    difficulty = data['difficulty']
    if difficulty == "easy":
        difficulty = 1
    elif difficulty == "medium":
        difficulty = 2
    elif difficulty == "hard":
        difficulty = 3
    elif difficulty == "very hard":
        difficulty = 4
    else:
        difficulty = 5
    additional_prompts = data['additional-prompt']
    result = QuestionGeneratorAI.generate_question(question_type, difficulty, additional_prompts)
    string_without_backticks = re.sub(r'^```json\n?|\n?```$', '', result, flags=re.MULTILINE)
    print(string_without_backticks)
    return JsonResponse({'question': string_without_backticks})
