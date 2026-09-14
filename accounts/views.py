from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def login_view(request):
    form = AuthenticationForm()
    return render (request,"accounts/login.html")

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    data = {
        'form':form
    }
    return render(request, 'accounts/signup.html', data)
