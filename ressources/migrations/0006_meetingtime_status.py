# Generated by Django 3.0.3 on 2020-08-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0005_auto_20200804_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingtime',
            name='status',
            field=models.CharField(choices=[('Libre', 'Libre'), ('Occupé', 'Occupé')], default='Libre', max_length=200, null=True, verbose_name='Etat'),
        ),
    ]
