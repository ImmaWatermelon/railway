# Generated by Django 4.1.6 on 2023-02-17 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prophetv2', '0022_stocks_risk_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockowned',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
