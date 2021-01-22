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
from users.views import CreateUser, LoginView, AdminUserView
from wallet.views import FundWallet, WithdrawWallet, AdminWalletView, WalletListView, MyWalletList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', CreateUser.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('client/fund/', FundWallet.as_view(), name='client_fund'),
    path('client/withdraw/', WithdrawWallet.as_view(), name='client_withdraw'),
    path('user/admin/', AdminUserView.as_view(), name='admin_user'),
    path('wallet/admin/', AdminWalletView.as_view(), name='admin_wallet'),
    path('wallet/list/', WalletListView.as_view(), name='wallet_list'),
    path('client/list/', MyWalletList.as_view(), name='my_wallet_list'),
]
