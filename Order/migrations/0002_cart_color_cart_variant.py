# Generated by Django 4.0.3 on 2022-03-23 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='variant',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
