# Generated by Django 5.1.6 on 2025-03-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.CharField(max_length=100),
        ),
    ]
