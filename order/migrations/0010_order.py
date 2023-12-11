# Generated by Django 4.1 on 2023-12-11 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_promo_diskon_promo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_harga', models.FloatField()),
                ('promo_used', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('processed', 'PROCESSED'), ('cancelled', 'CANCELLED'), ('done', 'DONE')], default='pending', max_length=15)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.item')),
            ],
        ),
    ]
