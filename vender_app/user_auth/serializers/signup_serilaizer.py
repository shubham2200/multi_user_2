from curses import meta
from dataclasses import field
from rest_framework import serializers
from user_auth.models.abstacts_user_model import *
from rest_framework.authtoken.models import Token

from user_auth.models.product_model import Product




class VendorSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ( "username",  "email", "is_vendor", "password2", "password",)
        # fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
# there are gone save
    def create(self, validated_data):
        print(validated_data)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            is_vendor=True
        )
        user.set_password(password)
        
        user.save()
        
        return user




class UserSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ( "username",  "email", "is_vendor", "password2", "password",)
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        print(validated_data)
        user = User(
            email=self.validated_data['email'],
            username= self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})

        user.set_password(password)
        user.is_user = True
        user.save()
        
        return user
    
