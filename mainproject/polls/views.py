from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.


def polls_list(request):
    question_list = Question.objects.order_by('id')
    context = {
        'question_list': question_list
    }
    return render(request, 'polls/polls_list.html', context)


def polls_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/polls.html", {'question': question})


def polls_if(request):
    return render(request, 'polls/polls_if.html')
