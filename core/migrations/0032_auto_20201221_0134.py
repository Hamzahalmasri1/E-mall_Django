# Generated by Django 3.0.6 on 2020-12-20 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20201221_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]