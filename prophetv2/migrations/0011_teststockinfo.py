# Generated by Django 4.1.6 on 2023-02-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prophetv2', '0010_delete_teststockinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestStockInfo',
            fields=[
                ('tradingName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('stockCode', models.CharField(max_length=100)),
                ('lastPrice', models.FloatField()),
                ('roe', models.FloatField()),
                ('marketcap', models.FloatField()),
                ('totalRev', models.FloatField()),
                ('pe', models.FloatField()),
                ('yieldPercent', models.FloatField()),
                ('sector', models.CharField(max_length=100)),
                ('gtiScore', models.FloatField()),
                ('oneYearChange', models.FloatField()),
            ],
        ),
    ]
