from django.contrib import admin
from .models import *  # Ensure that Users is the model class

admin.site.register(Users) 
admin.site.register(Customer) 
admin.site.register(Orders)

