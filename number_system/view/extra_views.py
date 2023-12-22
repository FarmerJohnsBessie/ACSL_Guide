from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def homepage(request):
    return render(request, 'pages/homepage.html')


@csrf_exempt
def test(request):
    return render(request, 'pages/test.html')

