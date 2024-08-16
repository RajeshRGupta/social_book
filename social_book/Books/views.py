from django.shortcuts import render,redirect
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from functools import wraps
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .form import *
from .models import *
from .serializers import *

# Create your views here.
@login_required(login_url='login')

def indexView(request):
    alldata=Books.objects.all()
    # authSell=list(filter((lambda x:x.public_visibility==True),alldata))
    data={'data':alldata}        
    return render(request, 'Books1.html',data)

@login_required(login_url='login')
def UploadBookView(request):
    # form=BookForm
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('/books')
    else:
        form=BookForm()
        print(form)
    return render(request,'Upload_Book.html',{'form':form})



@api_view(['GET','POST'])
@parser_classes([MultiPartParser, FormParser])
def UploadBookApiView(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)
     
    if request.method=='POST':
        print("Request data:-----", request.data)
        serializer=BooksSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Book uploaded successfully!','book':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






def check_my_book(view_fun):   
    @wraps(view_fun)
    def _wrapped_view(request):
        user=request.user
        if Books.objects.filter(user=request.user).exists():
            return view_fun(request)
        else:
            return HttpResponse('/bookUpload')
    return _wrapped_view


@login_required(login_url='login')  
@check_my_book
def MybooksView(request):
    mydata=Books.objects.filter(user=request.user)
    data={'data':mydata}        
    print(data)
    return render(request, 'MyBooks.html',data)


def sendMailView(request,pk):
    todata=Books.objects.filter(id=pk)
    data=list(map(lambda x:x.user,todata))[0]
    user=str(request.user)
    print(user)
    if request.method=='POST':
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        content=request.POST.get('content')
        
        if user!=email:
            send_mail(subject,content,user,[email],fail_silently=False)        
            return HttpResponse('sukjnsd')
        
    return render(request,"SendMail.html",{'data':data} )



