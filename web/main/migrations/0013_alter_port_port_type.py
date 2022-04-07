# Generated by Django 4.0.3 on 2022-04-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_port_port_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='port_type',
            field=models.CharField(choices=[('', 'Выберите тип...'), ('access', 'A'), ('trunk', 'T')], default='access', max_length=100, verbose_name='Тип оборудования'),
        ),
    ]
