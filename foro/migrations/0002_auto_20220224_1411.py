# Generated by Django 3.2 on 2022-02-24 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('normas', '0002_auto_20220224_1411'),
        ('foro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coments_foro',
            options={'verbose_name_plural': 'Comentarios'},
        ),
        migrations.RemoveField(
            model_name='coments_foro',
            name='themas',
        ),
        migrations.AddField(
            model_name='coments_foro',
            name='tema',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='normas.register_normativa'),
        ),
    ]
