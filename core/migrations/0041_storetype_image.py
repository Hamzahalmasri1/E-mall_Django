# Generated by Django 3.0.6 on 2020-12-24 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_product_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='storetype',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='StoresType-Images'),
        ),
    ]
