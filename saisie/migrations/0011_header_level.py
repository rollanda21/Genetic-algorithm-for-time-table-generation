# Generated by Django 3.0.3 on 2020-09-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saisie', '0010_group_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('Niveau 1', 'Niveau 1'), ('Niveau 2', 'Niveau 2'), ('Niveau 3', 'Niveau 3'), ('Niveau 4', 'Niveau 4'), ('Niveau 5', 'Niveau 5')], default='Niveau 1', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(blank=True, max_length=200, null=True, verbose_name='Semestre')),
                ('activity', models.CharField(blank=True, choices=[('Cours Magistral', 'Cours Magistral'), ('Travaux Dirigés', 'Travaux Dirigés'), ('Travaux Pratiques', 'Travaux Pratiques'), ('Contrôle Continu', 'Contrôle Continu'), ('Examens', 'Examens'), ('Soutenances', 'Soutenances'), ('Autre', 'Autre')], default='Cours Magistral', max_length=200, null=True, verbose_name='Activité')),
                ('academic_year', models.CharField(blank=True, max_length=200, null=True, verbose_name='Année académique')),
                ('level', models.ManyToManyField(to='saisie.Level')),
            ],
        ),
    ]
