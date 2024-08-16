from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
import random
from .form import *
from .models import *

# Create your views here.


def generate_otp():
    return str(random.randint(100000, 999999))


def OTPSend(otp_code,email):
    send_mail(
            'Your OTP Code',
            f'Your OTP code is {otp_code}.',
            'rkg9969541253@gmail.com', 
            [email],
            )

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email, password=password)
            if user is not None:
                otp_code=generate_otp()
                OTP.objects.create(user=user,otp_code=otp_code)
                OTPSend(otp_code,email)
                request.session['user_id'] = user.id
                return redirect('/verification')
    else:
        form = UserLoginForm()    
    return render(request, 'loginForm.html', {'form': form})


def Otpvafication(request):
    if request.method=="POST":
        otp_code=int(request.POST.get('otp_code'))
        user_id = request.session.get('user_id')
        try:
            otp=OTP.objects.get(user_id=user_id,otp_code=otp_code)
            if otp.is_valid():
                otp.delete()
                user=otp.user
                login(request,user)
                request.session.pop('user_id',None)
                return redirect('/AuthSell')
        except:
            otp.delete()
            request.session['all_try'] = AllTry
            return redirect('/verification')
    return render(request,'otpVarify.html')

def OTPResend(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/login')
    try:
        user=User.objects.get(id=user_id)
        otp_code=generate_otp()
        otp = OTP.objects.filter(user=user).last()
        if otp and otp.is_valid and not otp.resent:
            otp.resent=True
            otp.save()
        else:
            otp = OTP.objects.create(user=user, otp_code=otp_code)
        OTPSend(otp_code,email=user.email)
        return redirect('/verification') 
    except User.DoesNotExist:
        return redirect('/login')



def register(request):
    if request.method =='POST':
        form=UserRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form=UserRegistrationForm()
    return render(request,'registerForm.html',{'form': form})


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='login')
def AuthSellView(request):
    alldata=User.objects.all()
    authSell=list(filter((lambda x:x.public_visibility==True),alldata))
    data={'data':authSell}    
    
    print(data)
    
    return render(request,'AuthSell1.html',data)