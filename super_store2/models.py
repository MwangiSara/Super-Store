from django.db import models

# Create your models here.

class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name= models.CharField(max_length=255)
    user_phone= models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.user_name
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_phone = models.IntegerField(unique=True)
    customer_email = models.CharField(max_length=100,unique=True)
    class Meta:
        db_table = "Customer"
    def __str__(self):
        return self.customer_name
    
class Orders(models.Model):
    orders_id = models.AutoField(primary_key=True)
    orders_item = models.CharField(max_length=255)
    orders_amount = models.IntegerField()
    order_customer = models.ForeignKey(Customer, to_field='customer_phone', on_delete=models.CASCADE, db_column='order_customer_phone')
    orders_time = models.DateTimeField(auto_now=True)

    def formatted_date(self):
        return self.orders_time.strftime('%B %d, %Y at %I:%M %p')

    class Meta:
        db_table = "Orders"

    def __str__(self):
        return self.orders_item
