from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request,"posts/list.html",{"posts":posts})
    
def new(request):
    
    if request.method=="POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            #유저정보 넣기
            post.user = request.user
            post.save()
            return redirect("posts:list")
    else:
        post_form = PostForm()
    return render(request,"posts/form.html",{"post_form":post_form})
    
def like(request,id):
    post = Post.objects.get(id=id)
    #유저의 정보 담기
    me = request.user
    #좋아요 이미 눌렀음 취소
    #
    # if me in post.likes.all(): #내가 있니
    #     pass
    # else:
    #     pass
    
    if post in me.likeposts.all():#post가 있니
        # post.likes.remove(me) #post에서 me삭제
        me.likeposts.remove(post) 
    else:
        # post.likes.add(me)
        me.likeposts.add(post) #좋아요
    return redirect("posts:list")