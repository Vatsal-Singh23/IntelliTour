# Generated by Django 3.2.10 on 2024-03-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_booking_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='packageType',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
