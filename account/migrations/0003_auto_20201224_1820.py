# Generated by Django 3.0.6 on 2020-12-24 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20201221_0013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userregistration',
            options={'ordering': ['username']},
        ),
    ]
