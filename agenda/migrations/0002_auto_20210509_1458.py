# Generated by Django 3.2 on 2021-05-09 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitiespatient',
            name='report',
        ),
        migrations.AddField(
            model_name='activitiespatient',
            name='date',
            field=models.DateField(default=None, verbose_name='Fecha de actividad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitiespatient',
            name='image',
            field=models.ImageField(blank=True, upload_to='report/images/', verbose_name='Imagen reporte'),
        ),
        migrations.AddField(
            model_name='activitiespatient',
            name='record',
            field=models.FileField(blank=True, upload_to='report/audio/', verbose_name='Audio reporte'),
        ),
        migrations.AddField(
            model_name='activitiespatient',
            name='text',
            field=models.CharField(default=None, max_length=200, verbose_name='Texto reporte'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitiespatient',
            name='time',
            field=models.TimeField(default=None, verbose_name='Hora de actividad'),
            preserve_default=False,
        ),
    ]
