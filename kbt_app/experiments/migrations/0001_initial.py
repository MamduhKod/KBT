# Generated by Django 5.0.6 on 2024-06-18 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namn', models.CharField(max_length=50)),
                ('beskrivning', models.CharField(max_length=300)),
                ('datum', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperimentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Beteende', models.CharField(max_length=100)),
                ('Situation', models.DateField(max_length=100)),
                ('Konsekvens', models.DateField(max_length=100)),
                ('Experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Hypotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hypotes', models.CharField(max_length=300)),
                ('tro_pre', models.SmallIntegerField()),
                ('Experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Insikt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insikter', models.CharField(max_length=300)),
                ('tro_skillnad', models.SmallIntegerField()),
                ('Experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Kognition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('negativ_tanke', models.CharField(max_length=50)),
                ('antagande', models.CharField(max_length=300)),
                ('Experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultat', models.CharField(max_length=300)),
                ('tro_post', models.SmallIntegerField()),
                ('Experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.experiment')),
            ],
        ),
    ]
