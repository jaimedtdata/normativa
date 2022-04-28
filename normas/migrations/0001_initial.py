# Generated by Django 3.2 on 2022-04-26 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Estado de norma')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': 'Estado de Norma',
            },
        ),
        migrations.CreateModel(
            name='Grupo_Tipo_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Grupo de tipo de norma')),
                ('icono', models.FileField(blank=True, null=True, upload_to='iconos_grupo_normativa', verbose_name='Icono del grupo')),
                ('order', models.CharField(blank=True, max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': 'Grupo de Tipo de Norma',
            },
        ),
        migrations.CreateModel(
            name='Normativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norma', models.CharField(blank=True, max_length=200, null=True, verbose_name='Norma')),
                ('denominacion', models.TextField(max_length=300, verbose_name='Titulo')),
                ('base_legal', models.CharField(blank=True, max_length=200, null=True, verbose_name='Base Legal')),
                ('fecha_publicacion', models.DateField(blank=True, null=True, verbose_name='Publicacion')),
                ('document', models.FileField(blank=True, null=True, upload_to='Document_normativa', verbose_name='Documentos')),
                ('propiedad', models.CharField(choices=[('PU', 'Publico'), ('PI', 'Propiedad Intelectual')], default='PU', max_length=150)),
                ('descripcion', models.CharField(blank=True, max_length=700, null=True, verbose_name='Descripcion')),
                ('articulo', models.CharField(blank=True, max_length=200, null=True, verbose_name='Articulo')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.estado_normas', verbose_name='Estado de la Norma')),
            ],
            options={
                'verbose_name_plural': 'Normativa',
            },
        ),
        migrations.CreateModel(
            name='Topico_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre de topico')),
                ('button', models.CharField(max_length=150, verbose_name='Texto de botón para topico')),
                ('icono', models.FileField(blank=True, null=True, upload_to='iconos_topico_normativa', verbose_name='Icono del topico')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name_plural': 'Topico Principal de Norma',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Uso_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre de Categoria', max_length=200, verbose_name='Nombre de la Categoria')),
                ('order', models.CharField(blank=True, max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('topico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.topico_normas', verbose_name='Topico Norma')),
            ],
            options={
                'verbose_name_plural': 'Tipo de Uso',
            },
        ),
        migrations.CreateModel(
            name='Tipo_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre de Tipo de norma', max_length=200, verbose_name='Tipo norma')),
                ('order', models.CharField(blank=True, max_length=10, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.grupo_tipo_normas', verbose_name='Grupo Norma')),
            ],
            options={
                'verbose_name_plural': 'Tipo de Norma',
            },
        ),
        migrations.CreateModel(
            name='Subtipo_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre de subtipo')),
                ('order', models.CharField(blank=True, max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('tipo_uso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.tipo_uso_normas', verbose_name='Tipo Uso')),
            ],
            options={
                'verbose_name_plural': 'Subtipo de Uso',
            },
        ),
        migrations.CreateModel(
            name='Preguntas_Frecuentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Titulo de Consulta', max_length=200, verbose_name='Titulo de Consulta')),
                ('message', models.TextField(help_text='Respuesta', verbose_name='Respuesta')),
                ('validity_date_start', models.DateField(help_text='Fecha Inicio', verbose_name='Fecha Inicio')),
                ('validity_date_finish', models.DateField(help_text='Fecha Fin', verbose_name='Fecha Fin')),
                ('register_date_time', models.DateTimeField(auto_now_add=True, help_text='Fecha de Registro', verbose_name='Fecha de Registro')),
                ('tipo_norma', models.ManyToManyField(blank=True, related_name='preguntas', to='normas.Tipo_Normas', verbose_name='Tipo de norma')),
            ],
            options={
                'verbose_name_plural': 'Preguntas Frecuentes',
            },
        ),
        migrations.CreateModel(
            name='Palabra_Clave_Normas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Nombre Palabra Clave')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de actualización')),
                ('normativas', models.ManyToManyField(blank=True, related_name='keywords', to='normas.Normativa', verbose_name='Normativa')),
            ],
            options={
                'verbose_name_plural': 'Palabras Clave',
            },
        ),
        migrations.AddField(
            model_name='normativa',
            name='subtipo_uso',
            field=models.ManyToManyField(blank=True, related_name='normativas', to='normas.Subtipo_Normas', verbose_name='Subtipo de uso'),
        ),
        migrations.AddField(
            model_name='normativa',
            name='tipo_norma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.tipo_normas', verbose_name='Tipo de Norma'),
        ),
        migrations.AddField(
            model_name='grupo_tipo_normas',
            name='topico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='normas.topico_normas', verbose_name='Topico Norma'),
        ),
    ]
