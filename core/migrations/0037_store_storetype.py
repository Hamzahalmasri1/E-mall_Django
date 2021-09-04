# Generated by Django 3.0.6 on 2020-12-21 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20201221_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='storetype',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.StoreType', verbose_name='Store Type'),
            preserve_default=False,
        ),
    ]