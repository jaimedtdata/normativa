# Generated by Django 3.2 on 2022-04-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimember',
            name='first_surname',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='apimember',
            name='second_surname',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Apellido Materno'),
        ),
    ]
