from django.conf.urls import url
from django.shortcuts import get_object_or_404, redirect, render
from .models import Question
from .forms import PostForm
import joblib
import numpy as np
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
        di_list = ["감염 및 세균바이러스성 질환", "신생물", "혈액 및 조혈기관 장애", "내분비, 영양 및 대사 질환", "정신 및 행동장애", "신경계통의 질환", "눈 및 눈 부속기의 질환", "귀 및 유돌의 질환", "순환계통의 질환", "호흡계통의 질환",
                   "눈 질환", "귀 질환", "순환계통 질환", "소화 계통 질환", "피부 질환", "근골격계통 질환", "비뇨생식계통의 질환", "임신 출산관련 질환", "아동기의 질환", "염색체 질환", "기타 질환", "손상에 관한 질환", "특수 질환", "질병이환", "기타"]

        form = PostForm(request.POST)
        a = request.POST

        BMI = int(a["weight"])/(int(a["height"])/100)**2
        if BMI <= 18.5:
            BMI = 0
        elif BMI <= 25 and BMI > 18.5:
            BMI = 1
        elif BMI <= 30 and BMI > 25:
            BMI = 2
        elif BMI > 30:
            BMI = 3
        survey_value = [int(a["family_stroke"]), int(a["family_heart"]), int(a["family_highBlood"]), int(a["family_diabetes"]),
                        int(a["family_etc"]), int(a["drink_count"]), int(a["drink_amount"]), int(a["smoke_yn"]), int(a["smoke_amount"]), int(a["exercise_count"]), int(BMI)]
        loaded_model = joblib.load(
            "C:/Users/acc05/Desktop/Develop/OSA-ESG/mainproject/rf_model.pkl")
        print(survey_value)
        predict = loaded_model.predict_proba(
            np.array(survey_value).reshape(1, -1))

        s = [a[0][1] for a in predict]
        k = sorted(range(len(s)), key=lambda k: s[k], reverse=True)
        k = k[:5]
        diease_list = []
        for am in k:
            diease_list.append(di_list[am])
    else:
        form = PostForm()
    return render(request, 'polls/results.html', {'form': form, 'diease_list': diease_list})
