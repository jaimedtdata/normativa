# Generated by Django 3.2 on 2022-05-02 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_apimember_foreign_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apimember',
            name='identity',
            field=models.CharField(blank=True, help_text='DNI o RUC', max_length=16, verbose_name='Documento de Identidad'),
        ),
    ]
