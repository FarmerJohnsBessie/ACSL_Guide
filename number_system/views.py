from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    return render(request, 'base.html')


@csrf_exempt
def homepage(request):
    return render(request, 'pages/homepage.html')

