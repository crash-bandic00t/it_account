# Generated by Django 4.0.3 on 2022-04-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_port_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='port_dest_id',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID порта назначения'),
        ),
    ]
