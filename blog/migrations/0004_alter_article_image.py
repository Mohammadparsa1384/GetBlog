# Generated by Django 4.2.2 on 2025-05-01 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='بنر مقاله'),
        ),
    ]
