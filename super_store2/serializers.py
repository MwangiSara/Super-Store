# to convert data to python dictionaty
from .models import Customer,Orders
from rest_framework import serializers

#serializer for customer data
class Customerserializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

#seializer for orders data
class Ordersserializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Orders
		fields = '__all__'