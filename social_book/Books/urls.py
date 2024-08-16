from django.urls import path
from .views import *

urlpatterns = [
    path('books/',indexView,name='books'),
    path('bookUpload/',UploadBookView,name='bookUpload'),
    path('bookUploadapi/',UploadBookApiView,name='bookUploadapi'),
    path('Mybooks/',MybooksView,name='Mybooks'),
    path('sendMail/<int:pk>',sendMailView,name='sendMail'),
]