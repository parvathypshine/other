# Generated by Django 4.1 on 2022-11-13 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='comment',
        ),
    ]
