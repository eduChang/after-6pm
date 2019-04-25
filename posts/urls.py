from django.urls import path
from . import views

app_name="posts"
urlpatterns=[
    path('',views.list,name="list"),
    path('new/',views.new,name="new"),
    path('<int:id>/like/',views.like,name="like"),
    ]