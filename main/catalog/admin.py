from django.contrib import admin
from .models import Item, AdditionalPicture, Brand, Category, Accessory


#
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
    'brand', 'full_name', 'vendor', 'description', 'main_picture', 'category_name', 'price', 'slug', 'in_stock',)
    filter_horizontal = ('additional_pic', 'accessories',)  # Используйте horizontal для ManyToManyField

    # search_fields = ('name', 'brand1_name', 'brand2_name')
    # list_filter = ('brand1_name', 'brand2_name')


@admin.register(AdditionalPicture)
class AdditionalPictureAdmin(admin.ModelAdmin):
    list_display = []
    fields = ('picture', 'name')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'broad_name', 'slug', 'category_picture')


admin.site.register(Accessory)
