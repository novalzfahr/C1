# Generated by Django 4.1 on 2023-12-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0007_alter_userdatamodel_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatamodel',
            name='role',
            field=models.CharField(choices=[('admin', 'ADMIN'), ('pelanggan', 'PELANGGAN')], default='admin', max_length=9),
        ),
    ]
