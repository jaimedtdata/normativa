# Generated by Django 3.2 on 2022-05-02 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='identity',
            field=models.CharField(blank=True, help_text='DNI o RUC', max_length=16, verbose_name='Documento de Identidad'),
        ),
        migrations.AlterField(
            model_name='member',
            name='person_type',
            field=models.CharField(blank=True, choices=[('N', 'DNI'), ('J', 'RUC'), ('C', 'CARNET DE EXTRANJERÍA'), ('P', 'PASAPORTE')], default='N', help_text='Tipo de Persona', max_length=1, verbose_name='Tipo de Persona'),
        ),
    ]