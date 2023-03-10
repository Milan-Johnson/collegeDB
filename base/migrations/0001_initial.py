# Generated by Django 4.1.4 on 2023-01-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('headOfDepartmentn', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('emailId', models.CharField(max_length=50)),
                ('dateOfBirth', models.DateField(max_length=8)),
            ],
        ),
    ]
