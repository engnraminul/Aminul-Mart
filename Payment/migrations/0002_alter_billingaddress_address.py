# Generated by Django 4.0.3 on 2022-04-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='address',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
