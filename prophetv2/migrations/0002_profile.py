# Generated by Django 4.1.6 on 2023-02-14 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prophetv2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='prophetv2.user')),
                ('accountbalance', models.FloatField()),
                ('tutorialcompletion', models.BooleanField()),
            ],
        ),
    ]
