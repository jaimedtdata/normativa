# Generated by Django 3.2 on 2022-04-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normas', '0002_auto_20220420_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normativa',
            name='denominacion',
            field=models.TextField(max_length=300, verbose_name='Titulo'),
        ),
    ]