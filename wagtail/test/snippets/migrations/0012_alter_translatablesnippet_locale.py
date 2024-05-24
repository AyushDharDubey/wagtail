# Generated by Django 5.0.6 on 2024-06-21 06:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippetstests', '0011_nonautocompletesearchablesnippet'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translatablesnippet',
            name='locale',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale', verbose_name='locale'),
        ),
    ]