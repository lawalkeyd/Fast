"""Fast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.api import UserResource, AdminResource, ClientResource, LoginUser
from wallet.api import ClientFund, FundWallet, WithdrawWallet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginUser.as_list(), name='login'),
    path('register/', UserResource.as_list(), name='register'),
    path('api/admin/', AdminResource.as_list(), name='api_user_list'),
    path('api/admin/<pk>', AdminResource.as_detail(), name='api_admin_detail'),
    path('api/client/<pk>', ClientResource.as_detail(), name='api_client_detail'),
    path('api/wallet/client/', ClientFund.as_list(), name='api_wallet_list'),
    path('api/wallet/client/<pk>', ClientFund.as_detail(), name='api_wallet_detail'),    
    path('api/wallet/fund/', FundWallet.as_list(), name='api_fund_list'),
    path('api/wallet/withdraw/', WithdrawWallet.as_list(), name='api_withdraw_list'),
]
