# Generated by Django 4.1.6 on 2023-02-14 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prophetv2', '0005_alter_profile_user_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]