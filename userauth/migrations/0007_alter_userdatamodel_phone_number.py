# Generated by Django 4.1 on 2023-11-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_alter_userdatamodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatamodel',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]