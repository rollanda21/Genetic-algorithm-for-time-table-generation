# Generated by Django 3.0.3 on 2020-08-04 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0004_auto_20200731_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetingtime',
            options={'ordering': ('day',)},
        ),
    ]