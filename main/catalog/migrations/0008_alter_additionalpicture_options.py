# Generated by Django 5.0.6 on 2024-07-12 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_category_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalpicture',
            options={'verbose_name': 'Дополнительное фото', 'verbose_name_plural': 'Дополнительные фото'},
        ),
    ]
