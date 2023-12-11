from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..forms import BaseConversionForm, BaseCalculatorForm, AnswerSubmissionForm, UserForm, ProfileForm
from random import choice, randint
from api.models import Question
from api.serializers import QuestionSerializer
from django.shortcuts import render
from ..models import Profile, SolverProfile


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
        question = Question.objects.filter(type=question_type)
        if question.exists():
            question = choice(question)
            question = QuestionSerializer(question, many=False).data
        else:
            question = None

        # else:
        #     if question_type == "Computer_Number_Systems":
        #         question = NumberSystem.generate_question()  # Replace with your data source
        #         question['id'] = -1
        #         question['likes'] = 0
        #     else:
        #         question = Question.objects.filter(type=question_type)
        #         if question.exists():
        #             question = choice(question)
        #             question = QuestionSerializer(question, many=False).data
        #         else:
        #             question = None

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

def like(request, pk):
    question = Question.objects.get(id=pk)
    question.likes = question.likes + 1
    question.save()
    response_data = {'status': 'success', 'message': 'Object updated successfully'}
    return JsonResponse(response_data)

def view_question(request, pk):
    question = Question.objects.get(id=pk)
    return render(request, 'pages/question_generator/view_question.html', {'question': question})
