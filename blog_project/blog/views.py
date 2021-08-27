from django.http.response import HttpResponseRedirect
from .forms import PostNew
from .forms import UpdateForm
from .models import Post
from django.shortcuts import render,get_object_or_404

# Create your views here.
def home(request):
    mytext=Post.objects.all()
    params={'mytext':mytext}
    return render(request,'blog/home.html',params)

def post_detail(request,pk):
    mytext=Post.objects.all()
    post = get_object_or_404(Post, pk=pk)
    params={'mytext':mytext,'post':post}
    return render(request,'blog/post_detail.html',params)

def post_new(request):
    form=PostNew(request.POST or None)
    if form.is_valid():
        form.save()
        form=PostNew()

    params={'form':form}
    return render(request,'blog/post_new.html',params)

def post_update(request,pk):
    post=get_object_or_404(Post, pk=pk)
    form=UpdateForm(request.POST,instance=post)
    if form.is_valid():
        form.save()
        form=UpdateForm()

    params={"form":form }
    return render(request,'blog/post_update.html',params)

def post_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect("/")
    params={'post':post}
    return render(request,'blog/post_delete.html',params)
