from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('AuthSell')
    else:
        form = UserLoginForm()    
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method =='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form=UserRegistrationForm()
    return render(request,'register.html',{'form': form})



@login_required(login_url='TodoLogin')
def AuthSellView(request):
    alldata=User.objects.all()
    authSell=list(filter((lambda x:x.public_visibility==True),alldata))
    data={'data':authSell}    
    return render(request,'authSell.html',data)
    