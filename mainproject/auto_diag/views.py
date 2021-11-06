from django.shortcuts import render

# Create your views here.


def diagnosis(request):
    return render(request, 'diagnosis/diagnosis_if.html')
