from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('signup-vendor/', VendorCreateView.as_view(), name='signup-vendor'),
    path('signup-user/', UserCreateView.as_view(), name='signup-user'),
    path('custom-token/', CustomTokenView.as_view(), name='custom-token'),
    path('producr-create/', ProducatCreatView.as_view(), name='producr-create'),

]
