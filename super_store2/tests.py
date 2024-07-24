from django.test import TestCase
from .models import Customer, Orders
import coverage
# Create your tests here.
class CustomerTest(TestCase):
    def setUpTestData(self):
        customer = Customer.objects.create(
            customer_name="John Doe",
            customer_phone="710101010",
            customer_email="john.doe@example.com")
        
        self.assertEqual(customer.customer_name, "John Doe")
        self.assertEqual(customer.customer_phone, "1234567890")
        self.assertEqual(customer.customer_email, "john.doe@example.com")
        
class OrdersTest(TestCase):
    def setUpTestData(self):
        order = Orders.objects.create(
            orders_item= "Shoe",
            orders_amount = "5000",
            order_customer = "701010101"
        )
        self.assertEqual(order.orders_item, "Shoe")
        self.assertEqual(order.orders_amount, "5000")
        self.assertEqual(order.order_customer, "701010101")