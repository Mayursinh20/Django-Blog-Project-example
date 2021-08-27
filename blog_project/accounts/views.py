from accounts.forms import SignupPage
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render



# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupPage(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password = raw_password)
            login(request,user)
            return redirect('home')

    else:
        form = SignupPage()
    params = {'form':form}

    return render(request,'accounts/signup.html',params)