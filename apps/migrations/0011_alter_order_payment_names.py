# Generated by Django 3.2 on 2022-03-16 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_auto_20220316_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_payment',
            name='names',
            field=models.CharField(blank=True, help_text='Nombres O Razón Social', max_length=50, verbose_name='Nombres'),
        ),
    ]