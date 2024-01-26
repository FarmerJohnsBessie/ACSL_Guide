from django.shortcuts import render
from django.http import JsonResponse
import json


def study_materials(request):
    return render(request, 'pages/study_materials/study_materials.html')

def study_materials_topic(request, topic):
    return render(request, f'pages/study_materials/{topic}.html')

def check_answer(request, topic):
    data = json.loads(request.body)
    answer = data['user_answer']
    id = str(data['id'])
    print(answer,id)
    if topic == 'demo':
        if answer == 'wenhao':
            return JsonResponse({'result': 'Impressive'})
        elif answer == 'clement':
            return JsonResponse({'result': 'Better than wenhao'})
    elif topic == 'Computer_Number_Systems':
        if id == "1":
            if answer == "bryan":
                return JsonResponse({'result': 'correct'})
    else:
        return JsonResponse({'result': 'Wrong Answer'})
