# Generated by Django 3.2.9 on 2021-11-04 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_uploader', '0006_image_p_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='p_hash',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]