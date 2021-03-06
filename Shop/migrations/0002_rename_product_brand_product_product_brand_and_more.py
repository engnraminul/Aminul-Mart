# Generated by Django 4.0.3 on 2022-03-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_brand',
            new_name='product_brand',
        ),
        migrations.AddField(
            model_name='product',
            name='Product_slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='preview_text',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
