# Generated by Django 4.2.14 on 2024-07-18 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_store2', '0006_alter_users_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='Customer',
        ),
        migrations.AlterModelTable(
            name='orders',
            table='Orders',
        ),
        migrations.AlterModelTable(
            name='users',
            table='Users',
        ),
    ]
