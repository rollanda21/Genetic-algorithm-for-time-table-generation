# Generated by Django 3.0.3 on 2020-08-04 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saisie', '0005_auto_20200731_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='status',
            field=models.CharField(choices=[('actif', 'actif'), ('Desactive', 'desactive'), ('soumis', 'soumis'), ('signe', 'signe'), ('en_attente', 'en_attente')], default='en_attente', max_length=200, null=True),
        ),
    ]