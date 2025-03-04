# Generated by Django 5.0.6 on 2024-07-11 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_category_options_remove_category_brand1_items_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='additional_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('main_picture', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='additionalpicture',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.item'),
        ),
    ]
