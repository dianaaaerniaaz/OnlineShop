# Generated by Django 4.1.7 on 2023-02-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.CharField(max_length=255, null=True),
        ),
    ]