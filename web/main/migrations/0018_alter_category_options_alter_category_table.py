# Generated by Django 4.0.3 on 2022-04-11 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_category_alter_port_dest_port_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]
