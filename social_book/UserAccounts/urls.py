from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_view,name='login'),
    path('verification/', Otpvafication,name='verification'),
    path('resend_otp/', OTPResend,name='resend_otp'),
    path('register/', register,name='register'),
    path('logout/', log_out,name='logout'),
    path('AuthSell/', AuthSellView,name='AuthSell'),
]