# Generated by Django 4.0.3 on 2022-04-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_complex_vlan_delete_commutation_remove_port_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VlanToPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Vlan на порту',
                'db_table': 'vlan-to-port',
            },
        ),
        migrations.AlterUniqueTogether(
            name='vlan',
            unique_together={('vlan_id', 'complex')},
        ),
    ]