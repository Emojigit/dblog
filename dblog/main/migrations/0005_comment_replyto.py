# Generated by Django 4.0.4 on 2022-05-10 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='replyto',
            field=models.ForeignKey(default=None, help_text='Replying to', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.comment'),
        ),
    ]
