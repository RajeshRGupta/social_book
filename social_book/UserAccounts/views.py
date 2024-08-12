from django.shortcuts import render

# Create your views here.


def login(request):
    context={'username':'admin','password':1}
    return render(request,'login.html',context)
