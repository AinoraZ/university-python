# Generated by Django 3.0.4 on 2020-05-20 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20200521_0228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materials',
            name='cost',
        ),
    ]