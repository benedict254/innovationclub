# Generated by Django 3.0.7 on 2020-09-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]