from rest_framework import generics, status
from .serializers import WalletSerializer
from .models import Wallet
from users.models import Userss
from rest_framework.views import APIView
import requests
import settings
from rest_framework.response import Response


class FundWallet(APIView):
    def post(self, request):        
        user_id = request.data.get('id')
        user = Userss.objects.get(id = user_id)
        if user.is_superuser:
            return Response({"error": "You don't have the permission to do this"}, status=status.HTTP_401_UNAUTHORIZED)        
        currency = request.data.get('currency')
        amount = request.data.get('amount')
        if user.is_noob:
            if user.main_currency == currency:
                wallet, created = Wallet.objects.get_or_create(user=user, currency=currency)
                wallet.amount += float(amount)
                wallet.save()
                return Response({"user": user.id})
            else:
                r = requests.get('https://data.fixer.io/api/latest?access_key=' + settings.EMBEDLY_KEY)
        if user.is_elite:
            wallet, created = Wallet.objects.get_or_create(user=user, currency=currency)
            wallet.amount += float(amount)
            wallet.save()
            return Response({"user": user.id})
        
class MyWalletList(generics.ListAPIView):
    serializer_class = WalletSerializer
    model = Wallet

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = self.model.objects.filter(user__id=user_id)
        return queryset.order_by('-post_time')


class WithdrawWallet(APIView):
    def post(self, request):
        if request.user.is_superuser:
            return Response({"error": "You don't have the permission to do this"}, status=status.HTTP_401_UNAUTHORIZED)
        user = request.user
        currency = request.data.get('currency')
        amount = request.data.get('amount')
        if user.is_noob:
            if user.main_currency == currency:
                wallet, created = Wallet.objects.get_or_create(user=user, currency=currency)
                wallet.amount +- float(amount)
                wallet.save()
                return Response({"user": user.id})
            else:
                r = requests.get('https://data.fixer.io/api/latest?access_key=' + settings.EMBEDLY_KEY)
        if user.is_elite:
            wallet, created = Wallet.objects.get_or_create(user=user, currency=currency)
            wallet.amount -= float(amount)
            wallet.save()
            return Response({"user": user.id})  

class WalletListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = WalletSerializier 

class AdminWalletView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = WalletSerializier                      