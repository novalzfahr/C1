# Generated by Django 4.1 on 2023-11-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0005_alter_userdatamodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatamodel',
            name='name',
            field=models.CharField(default='NewUser', max_length=100),
        ),
    ]