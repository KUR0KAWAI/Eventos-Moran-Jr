# Generated by Django 5.0.3 on 2024-03-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Eventos',
            },
        ),
    ]
