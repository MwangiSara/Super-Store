# Generated by Django 3.1.7 on 2024-07-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_store2', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orders_id', models.AutoField(primary_key=True, serialize=False)),
                ('orders_item', models.CharField(max_length=255)),
                ('orders_amount', models.IntegerField()),
                ('orders_time', models.DateTimeField()),
            ],
        ),
    ]
