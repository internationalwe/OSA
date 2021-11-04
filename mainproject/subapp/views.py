from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def sub(request):
    return render(request, 'subapp/subView.html')


def sub_index(request, sub_id):
    return render(request, 'subapp/sublistView.html', {'sub_id' : sub_id})
