# Generated by Django 4.0.4 on 2022-05-09 03:06

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=50, unique=True, validators=[main.models.slug_validate_even]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
