# Generated by Django 2.1.5 on 2019-01-25 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.AlterModelOptions(
            name='aboutme',
            options={'verbose_name_plural': 'About Me'},
        ),
        migrations.AlterModelOptions(
            name='expertise',
            options={'verbose_name_plural': 'Expertise'},
        ),
    ]
