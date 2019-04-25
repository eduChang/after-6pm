from django.urls import path
from . import views
app_name="accounts"

#회원가입 로그인 로그아웃
urlpatterns=[
    path('login/',views.login, name="login"),
    path('signup/',views.signup,name="signup"),
    ]