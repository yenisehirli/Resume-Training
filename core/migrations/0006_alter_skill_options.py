# Generated by Django 4.2.4 on 2023-09-04 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('order',), 'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]