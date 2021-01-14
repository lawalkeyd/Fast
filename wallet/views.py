from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import WalletSerializer
from .models import Wallet

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def wallet_list(request):
    """
    List all wallets, or create a new wallet.
    """
    if request.user.is_admin == False:
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        wallets = Wallet.objects.all()
        serializer = WalletSerializer(wallets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fund_mywallet(request):
    """
    Allow noob and elite users fund wallets
    """
    if request.user.is_admin == True:
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'POST':
        serializer = WalletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
