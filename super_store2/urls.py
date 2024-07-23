from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *
from rest_framework import routers


router = routers.DefaultRouter() #adding default api root view
router.register(r'customer', Customers_api)
router.register(r'order', Orders_api)


urlpatterns = [
     path('', views.index , name='home'), #route for index.php 
     path('login/', views.login , name='login'),#route for login
     path('register/', views.register , name='register'),#route for register
     path('customers/', views.customers , name='customers'),#route for register
     path('orders/', views.orders , name='orders'),#route for register
     path('oidc/', include('mozilla_django_oidc.urls')),#route for mozilla_django_oidc
     path('', include(router.urls)),#route for apis
     path('customer/', Customers_api.as_view({'get': 'list'}), name='customer'),#route for customer api
     path('order/', Orders_api.as_view({'get': 'list'}), name='order')#route for order api
]
