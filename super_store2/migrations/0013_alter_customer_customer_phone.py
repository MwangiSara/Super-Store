# Generated by Django 4.0.5 on 2024-07-23 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_store2', '0012_alter_customer_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.IntegerField(unique=True),
        ),
    ]
