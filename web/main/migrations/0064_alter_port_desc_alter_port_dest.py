# Generated by Django 4.0.3 on 2022-05-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_port_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='desc',
            field=models.TextField(blank=True, default='-', max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='port',
            name='dest',
            field=models.CharField(blank=True, default='-', max_length=100, verbose_name='Куда'),
        ),
    ]
