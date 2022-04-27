# Generated by Django 4.0.3 on 2022-04-25 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_alter_port_dest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование комплекса')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Комплекс',
                'verbose_name_plural': 'Комплексы',
                'db_table': 'complex',
            },
        ),
        migrations.CreateModel(
            name='Vlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlan_id', models.PositiveIntegerField(verbose_name='Номер vlan')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование vlan')),
                ('desc', models.TextField(blank=True, max_length=200, verbose_name='Описание')),
                ('complex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vlan', to='main.complex', verbose_name='Комплекс')),
            ],
            options={
                'verbose_name': 'Vlan',
                'verbose_name_plural': 'Vlans',
                'db_table': 'vlan',
            },
        ),
        migrations.DeleteModel(
            name='Commutation',
        ),
        migrations.RemoveField(
            model_name='port',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='equipment',
            name='complex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='main.complex', verbose_name='Комплекс'),
        ),
    ]