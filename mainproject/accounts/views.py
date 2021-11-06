from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from accounts.forms import UserForm


# Create your views here.

def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == "POST":
        # UserForm으로 만든 형태를 form으로 저장
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('main:main')
    else:
        form = UserForm()
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'accounts/signup.html', {'form': form})
