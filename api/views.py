from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question
from .serializers import QuestionSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response("Routes")

@api_view(['GET'])
def getQuestions(request):
    serializer = QuestionSerializer(Question.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getQuestion(request, pk):
    serializer = QuestionSerializer(Question.objects.get(id=pk), many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createQuestion(request):
    data = request.data
    question = Question.objects.create(
        question=data['question'],
        type=data['type'],
        is_multiple_choice=data['is_multiple_choice'],
        steps=data['steps'],
        answer=data['answer'],
        likes=data['likes'],
        difficulty=data['difficulty'],
        num_choices=data['num_choices'],
        choices=data['choices'],
    )
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)

