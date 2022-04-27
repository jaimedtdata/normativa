# Generated by Django 3.2 on 2022-04-26 20:13

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
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo del video')),
                ('embed', models.TextField()),
                ('caratula', models.FileField(blank=True, null=True, upload_to='caratulas', verbose_name='Caratula')),
                ('descripcion', models.CharField(blank=True, max_length=700, null=True, verbose_name='Descripcion del video')),
                ('fecha_publicacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de publicación')),
            ],
            options={
                'verbose_name_plural': 'Cursos',
            },
        ),
    ]
