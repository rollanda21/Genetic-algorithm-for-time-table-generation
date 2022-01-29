# Generated by Django 3.0.3 on 2020-08-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saisie', '0006_auto_20200804_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, max_length=200, null=True, verbose_name='Semestre')),
                ('activity', models.CharField(blank=True, max_length=200, null=True, verbose_name='Activité')),
                ('academic_year', models.CharField(blank=True, max_length=200, null=True, verbose_name='Année académique')),
            ],
        ),
    ]