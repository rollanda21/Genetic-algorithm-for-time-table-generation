# Generated by Django 3.0.3 on 2020-07-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0002_auto_20200721_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='grade',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='instructor',
            name='status',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('Indisponible', 'Indisponible')], default='Disponible', max_length=200, null=True),
        ),
    ]
