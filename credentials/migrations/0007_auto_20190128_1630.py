# Generated by Django 2.1.5 on 2019-01-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0006_auto_20190127_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='credentials/static/img'),
        ),
    ]
