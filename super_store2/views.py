from django.shortcuts import *
from .forms import *
from .models import *
from rest_framework import viewsets
from .serializers import *
import requests
from django.urls import *
import africastalking
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# home function
def index(request):
    return render(request, 'index.html')
# login function
def login(request):
    return render(request, 'login.html')
# register function
def register(request):
    if request.method == 'POST':
        form = Users_form(request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
        form = Users_form()
    return render(request, 'register.html', {'form':form})

# customers function
def customers(request):
    api_url = request.build_absolute_uri('/customer/')
    # print("api url is:",api_url)
    response = requests.get(api_url)
    customers_info = response.json()
    return render(request, 'customers.html', {'customers_info':customers_info})

# get, post, put and delete customers api class
class Customers_api(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer
    # print("Customer queryset is",queryset)

# orders function
def orders(request):
    api_url = request.build_absolute_uri('/order/')
    # print("api url is:",api_url)
    response = requests.get(api_url)
    orders_info = response.json()
    # print("orders_info are:",orders_info)
    customer_api_url = request.build_absolute_uri('/customer/')
    customers_reponse = requests.get(customer_api_url)
    customers_info = customers_reponse.json()
    # print("customers_info:",customers_info)
    return render(request, 'orders.html', {'orders_info':orders_info, 'customers_info':customers_info})

# get, post, put and delete orders api class
class Orders_api(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = Ordersserializer
    # print("Orders queryset is",queryset)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            customer = Customer.objects.get(customer_phone=order.order_customer.customer_phone)  
            phone = f'+245{customer.customer_phone}'
            message = f"Dear {customer.customer_name}, your order for {order.orders_item} has been successfully placed."
            # print(message)
            send_sms(phone, message)
            return Response(data= serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#africastalking sms config
africastalking.initialize(
    username=settings.AFRICASTALKING_USERNAME,
    api_key=settings.AFRICASTALKING_API_KEY
)
sms = africastalking.SMS
#africastalking sending sms function
def send_sms(phone, message):
    recipients = [phone]
    sender = "AFRICASTKNG"
    try:
        response = sms.send(message, recipients)
        print(response)
    except Exception as error:
        print("Error is ", error)






