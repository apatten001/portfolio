# Generated by Django 2.1.5 on 2019-01-27 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0005_socialmedia_social_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='percentage',
            field=models.IntegerField(default=0, help_text='percentage of competency for this skill'),
        ),
    ]
