# Generated by Django 5.0.1 on 2024-02-06 22:57

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='product_name', unique=True, verbose_name='slug'),
        ),
    ]
