# Generated by Django 5.1.2 on 2025-02-01 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_accessory_item_accessories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accessory',
            options={'verbose_name': 'Состав', 'verbose_name_plural': 'Состав'},
        ),
        migrations.AddField(
            model_name='category',
            name='whatfor1',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='whatfor1_num',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='whatfor2',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='whatfor2_num',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
