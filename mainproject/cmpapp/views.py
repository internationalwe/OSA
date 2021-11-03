from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def cmplist(request):
    return HttpResponse("Hello!")

def cmp(request):
    return HttpResponse("Hello!")