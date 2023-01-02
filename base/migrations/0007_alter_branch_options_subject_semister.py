# Generated by Django 4.1.4 on 2023-01-02 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_student_alter_faculty_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name_plural': 'branches'},
        ),
        migrations.AddField(
            model_name='subject',
            name='semister',
            field=models.CharField(default='S3', max_length=2),
            preserve_default=False,
        ),
    ]
