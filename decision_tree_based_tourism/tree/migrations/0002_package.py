# Generated by Django 3.2.10 on 2024-03-02 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('image1', models.FileField(null=True, upload_to='')),
                ('image2', models.FileField(null=True, upload_to='')),
                ('image3', models.FileField(null=True, upload_to='')),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.CharField(max_length=10, null=True)),
                ('duration', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
