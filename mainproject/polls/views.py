from django.conf.urls import url
from django.shortcuts import get_object_or_404, redirect, render
from .models import Question
from .forms import PostForm

# Create your views here.


def polls_list(request):
    question_list = Question.objects.order_by('id')
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/polls_list.html', context)


def polls_if(request):
    return render(request, 'polls/polls_if.html')


def results(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        print(request.POST)
    else:
        form = PostForm()
    return render(request, 'polls/results.html', {'form': form})
