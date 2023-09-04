# Generated by Django 4.2.4 on 2023-09-04 01:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_imagesetting_options_imagesetting_created_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(blank=True, default='', help_text='this is help text', max_length=254, verbose_name='Name')),
                ('percentage', models.IntegerField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Percentage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
