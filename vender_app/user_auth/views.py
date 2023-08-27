from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from user_auth.models.abstacts_user_model import *
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from drf_yasg.utils import swagger_auto_schema
from user_auth.serializers.signup_serilaizer import VendorSignupSerializer, UserSerializer, UserSignupSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import  IsAuthenticated
from user_auth.models.product_model import Product
from user_auth.serializers.signup_serilaizer import ProductSerilaizer

from user_auth.permission import IsVendorUser 




class VendorCreateView(generics.GenericAPIView):
    manage_signup = VendorSignupSerializer
    @swagger_auto_schema(request_body=manage_signup)
    def post(self,request, *args, **kwargs):
        seri = self.manage_signup(data= request.data)
        if seri.is_valid(raise_exception=True):
            user = seri.save()
            key = CustomToken.objects.get(user=user).key
            print(key)
            
           
            return JsonResponse({
            'user':seri.data,
            'token':key,
            'massage':'done Vendor'
            })
        



class UserCreateView(generics.GenericAPIView):
    manage_signup = UserSignupSerializer
    @swagger_auto_schema(request_body=manage_signup)
    def post(self,request, *args, **kwargs):
        seri = self.manage_signup(data= request.data)
        if seri.is_valid(raise_exception=True):
            user = seri.save()
            key = CustomToken.objects.get(user=user).key
            print(key)
            
           
            return JsonResponse({
            'user':seri.data,
            'token':key,
            'massage':'done User'
            })
        
    
class CustomTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serialize = self.serializer_class(data = request.data , context = {'request':request})
        serialize.is_valid(raise_exception=True)
        user = serialize.validated_data['user']
        token , created= CustomToken.objects.get_or_create(user=user)
        return JsonResponse({
            'token':token.key,
            'user_id':user.pk,
            'is_vendor':user.is_vendor
        })





class ProducatCreatView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated&IsVendorUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerilaizer