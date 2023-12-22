from django.shortcuts import render
from django.http import JsonResponse
import json


def study_materials(request):
    return render(request, 'pages/study_materials.html')

def study_materials_topic(request, topic):
    return render(request, f'pages/study_materials/{topic}.html')

def check_answer(request, topic):
    data = json.loads(request.body)
    answer = data['user_answer']
    print(answer)
    if topic == 'demo':
        if answer == 'wenhao':
            return JsonResponse({'answer': 'Impressive'})
        elif answer == 'clement':
            return JsonResponse({'answer': 'Better than wenhao'})
    else:
        return JsonResponse({'answer': 'Wrong Answer'})
