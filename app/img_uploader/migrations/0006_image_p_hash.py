# Generated by Django 3.2.9 on 2021-11-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_uploader', '0005_alter_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='p_hash',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]