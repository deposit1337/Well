# Generated by Django 5.1.2 on 2025-01-18 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_item_is_active_alter_category_broad_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='accessories',
            field=models.ManyToManyField(blank=True, to='catalog.accessory'),
        ),
    ]
