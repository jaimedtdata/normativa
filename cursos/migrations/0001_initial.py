# Generated by Django 3.2 on 2022-04-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Titulo del video')),
                ('embed', models.CharField(max_length=1000, verbose_name='Embed del video')),
                ('descripcion', models.CharField(blank=True, max_length=700, null=True, verbose_name='Descripcion del video')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name_plural': 'Foro',
            },
        ),
    ]
