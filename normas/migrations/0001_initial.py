# Generated by Django 3.2 on 2022-03-04 10:26

from django.db import migrations, models
import django.db.models.deletion
import normas.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(help_text='Nombre de Categoria', max_length=200, verbose_name='Nombre de la Categoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': '0.Normas - Tipo de Uso',
            },
        ),
        migrations.CreateModel(
            name='Categories_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(help_text='Nombre de Categoria', max_length=200, verbose_name='Nombre de la Categoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('area_name', models.ManyToManyField(help_text='Area Corresponde', to='normas.Areas_Normas', verbose_name='Area')),
            ],
            options={
                'verbose_name_plural': '1.Normas - Sub Tipo de Uso',
            },
        ),
        migrations.CreateModel(
            name='Location_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_name', models.CharField(help_text='Nombre Locacion', max_length=200, verbose_name='Locacion')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': '3.Normas - Locacion',
            },
        ),
        migrations.CreateModel(
            name='Register_Normativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norma', models.CharField(max_length=200, verbose_name='Norma')),
                ('name_denom', models.TextField(verbose_name='Denominacion')),
                ('base_legal', models.CharField(max_length=200, verbose_name='Base Legal')),
                ('fecha_publi', models.DateField(verbose_name='Publicacion')),
                ('document', models.FileField(null=True, upload_to='Document_normativa', verbose_name='Documentos')),
                ('es_foro', models.BooleanField(default=False, verbose_name='Es un foro')),
                ('es_vigente', models.BooleanField(default=False, verbose_name='Esta vigente')),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': '6.Normas Registradas-Frontend',
                'db_table': 'register_normativa',
            },
        ),
        migrations.CreateModel(
            name='Subcategories_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(help_text='Nombre de sub Categoria', max_length=200, verbose_name='sub Categoria')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('order', models.CharField(blank=True, max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': '2.Normas - Subtipo De Normativa',
            },
        ),
        migrations.CreateModel(
            name='SubNormativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norma', models.CharField(max_length=200, verbose_name='Normativa')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('norma_sub', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='normas.subcategories_normas', verbose_name='Sub Normativa')),
            ],
            options={
                'verbose_name_plural': '5.Normas-Normativa',
            },
        ),
        migrations.CreateModel(
            name='Register_Palabraclave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre Palabra Clave')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('normativas', models.ManyToManyField(related_name='keywords', to='normas.Register_Normativa', verbose_name='Normativa')),
            ],
            options={
                'verbose_name_plural': '7.Normas Registradas-Palabras Clave',
                'db_table': 'register_palabclave',
            },
        ),
        migrations.AddField(
            model_name='register_normativa',
            name='tipo_norma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.subcategories_normas', verbose_name='Tipo de Norma'),
        ),
        migrations.AddField(
            model_name='register_normativa',
            name='tipo_uso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.areas_normas', verbose_name='Tipo Uso'),
        ),
        migrations.CreateModel(
            name='Policies_usage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Titulo de Consulta', max_length=200, verbose_name='Titulo de Consulta')),
                ('message', models.TextField(help_text='Respuesta', verbose_name='Respuesta')),
                ('validity_date_start', models.DateField(help_text='Fecha Inicio', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha Fin', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('norma', models.ManyToManyField(related_name='preguntas_frecuentes', to='normas.Register_Normativa')),
            ],
            options={
                'verbose_name_plural': 'Preguntas Frecuentes',
            },
        ),
        migrations.CreateModel(
            name='Master_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norma_rne', models.CharField(blank=True, help_text='Nombre RNE - Norma', max_length=50, verbose_name='RNE-Norma')),
                ('norma_name', models.CharField(help_text='Nombre de Norma', max_length=200, verbose_name='Norma')),
                ('validity_date_start', models.DateField(help_text='Fecha Publicacion', verbose_name='Fecha Publicacion')),
                ('keywords', models.CharField(blank=True, help_text='Palabras Clave', max_length=200, verbose_name='Registre palabras clave')),
                ('file', models.FileField(help_text='Suba el archivo o base legal', upload_to=normas.models.upload_file, verbose_name='File')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('area_name', models.ForeignKey(help_text='registro de Tipo de Uso', on_delete=django.db.models.deletion.CASCADE, to='normas.areas_normas', verbose_name='Tipo de Uso')),
                ('category_name', models.ForeignKey(help_text='registro Sub Tipo de Uso', on_delete=django.db.models.deletion.CASCADE, to='normas.categories_normas', verbose_name='Sub Tipo de Uso')),
                ('location_name', models.ForeignKey(help_text='Registro de Locacion', on_delete=django.db.models.deletion.CASCADE, to='normas.location_normas', verbose_name='Locacion')),
                ('subcategory_name', models.ForeignKey(help_text='registro Tipo de Normativa', on_delete=django.db.models.deletion.CASCADE, to='normas.subcategories_normas', verbose_name='Tipo de Normativa')),
            ],
            options={
                'verbose_name_plural': '4.Registrar Normas',
            },
        ),
    ]
