# Generated by Django 4.1 on 2023-11-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_alter_userdatamodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatamodel',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
