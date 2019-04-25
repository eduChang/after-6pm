from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login as auth_login
# Create your views here.
def login(request):
    # 로그인을 하기 위한 폼 =>create와 비슷 
    if request.method=="POST":
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            # 유저정보 넣기
            auth_login(request,login_form.get_user())
            return redirect("accounts:login")
    else:
        login_form = AuthenticationForm()
    return render(request,"accounts/login.html",{"login_form":login_form})
    
def signup(request):
    if request.method=="POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("accounts:login")
        #검증에 통과하지 못한다면통과
    else:
        user_form = UserCreationForm()
    return render(request,"accounts/signup.html",{"user_form":user_form})
    