# Generated by Django 3.0.6 on 2020-12-20 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20201220_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Products-images/None/'),
        ),
    ]
