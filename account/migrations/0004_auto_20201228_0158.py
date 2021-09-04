# Generated by Django 3.0.6 on 2020-12-27 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20201224_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='address',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='city',
            field=models.CharField(blank=True, choices=[('Amman', 'Amman'), ('Irbid', 'Irbid'), ('Ajloun', 'Ajloun'), ('Jerash', 'Jerash'), ('Mafraq', 'Mafraq'), ('Balqa', 'Balqa'), ('Zarqa', 'Zarqa'), ('Madaba', 'Madaba'), ('Karak', 'Karak'), ('Tafilah', 'Tafilah'), ("Ma/'an", "Ma/'an"), ('Aqaba', 'Aqaba')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userregistration',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Zip Code'),
        ),
    ]
