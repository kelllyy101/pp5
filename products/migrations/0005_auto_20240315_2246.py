# Generated by Django 3.2 on 2024-03-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20240309_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(),
        ),
    ]
