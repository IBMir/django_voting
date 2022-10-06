from django.shortcuts import render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse(f'Вы смотрите на вопрос {question_id}')


def results(request, question_id):
    return HttpResponse(f'Вы смотрите на результаты вопроса {question_id}')


def vote(request, question_id):
    return HttpResponse(f'Вы отвечаете на вопрос {question_id}')