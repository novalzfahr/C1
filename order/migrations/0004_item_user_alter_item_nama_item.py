# Generated by Django 4.1 on 2023-12-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_remove_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='nama_item',
            field=models.CharField(default='', max_length=200),
        ),
    ]