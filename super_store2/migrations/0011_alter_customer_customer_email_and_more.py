# Generated by Django 4.0.5 on 2024-07-23 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_store2', '0010_remove_customer_customer_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orders_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]