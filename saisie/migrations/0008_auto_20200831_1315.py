# Generated by Django 3.0.3 on 2020-08-31 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saisie', '0007_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='activity',
            field=models.CharField(blank=True, choices=[('Cours Magistral', 'Cours Magistral'), ('Travaux Dirigés', 'Travaux Dirigés'), ('Travaux Pratiques', 'Travaux Pratiques'), ('Contrôle Continu', 'Contrôle Continu'), ('Examens', 'Examens'), ('Soutenances', 'Soutenances'), ('Autre', 'Autre')], default='Cours Magistral', max_length=200, null=True, verbose_name='Activité'),
        ),
    ]