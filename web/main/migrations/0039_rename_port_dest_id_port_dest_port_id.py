# Generated by Django 4.0.3 on 2022-04-14 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_port_port_dest_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='port',
            old_name='port_dest_id',
            new_name='dest_port_id',
        ),
    ]
