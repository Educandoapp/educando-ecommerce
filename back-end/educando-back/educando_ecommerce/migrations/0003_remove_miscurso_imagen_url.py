# Generated by Django 4.2.1 on 2023-05-20 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educando_ecommerce', '0002_alter_contacto_mensaje_alter_contacto_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miscurso',
            name='imagen_url',
        ),
    ]
