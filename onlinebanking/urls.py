"""onlinebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from onlinebankmanager.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',Home.as_view()),
    url(r'^login/$',Login.as_view()),
    url(r'^accounts/auth/$',Athe.as_view(),name='athenticate'),
    url(r'^accounts/home/$',LoginHome.as_view(),name='loginhome'),
    url(r'^accounts/logout/$',LogoutOption.as_view()),
    url(r'^accounts/register/$',CreateAccount.as_view(),name='reg'),
    url(r'^accounts/deposite/$',DepositeMoney.as_view(),name='deposite'),
    url(r'^accounts/withdraw/$',WithDrawMoney.as_view(),name='withdraw'),
    url(r'^accounts/transaction/$',allTransation.as_view(),name='transaction'),
    url(r'^accounts/balanceCheck/$',getBalance.as_view(),name='checkbalance'),
    url(r'^accounts/invalid/$',invalidClass.as_view(),name='invalid'),
    url(r'^accounts/userDetail/$',userDetail.as_view(),name='userdetail')




]
