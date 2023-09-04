# Generated by Django 4.2.4 on 2023-09-04 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='Name')),
                ('email', models.EmailField(blank=True, default='', max_length=254, verbose_name='Email')),
                ('subject', models.CharField(blank=True, default='', max_length=254, verbose_name='Subject')),
                ('message', models.TextField(blank=True, default='', verbose_name='Message')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
