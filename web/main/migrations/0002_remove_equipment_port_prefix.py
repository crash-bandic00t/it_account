# Generated by Django 4.0.3 on 2022-03-31 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='port_prefix',
        ),
    ]
