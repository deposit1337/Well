# Generated by Django 5.0.6 on 2024-07-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_item_in_stock_item_price_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=None, max_length=255, null=True),
        ),
    ]
