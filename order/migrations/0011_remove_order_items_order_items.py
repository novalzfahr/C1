# Generated by Django 4.1 on 2023-12-11 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='order.item'),
        ),
    ]
