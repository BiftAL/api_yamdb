# Generated by Django 2.2.16 on 2022-11-09 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0007_auto_20221104_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['-id'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]