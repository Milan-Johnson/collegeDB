# Generated by Django 4.1.4 on 2023-01-02 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0003_delete_departments_delete_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branchCode', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('headOfDepartment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectCode', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=50)),
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
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.branch')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.departments')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyId', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('emailId', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.departments')),
                ('subject', models.ManyToManyField(to='base.subject')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.departments'),
        ),
    ]
