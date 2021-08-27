from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<h1>Home PAge</h1>")
    return render(request,'index.html')