from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'mainapp/mainView.html')


def about(request):
    return render(request, 'mainapp/about.html')
