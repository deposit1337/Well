from rest_framework import serializers
from .models import Brand, Category, Item, AdditionalPicture


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class AdditionalPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalPicture
        fields = ['picture']


class ItemSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    additional_pic = AdditionalPictureSerializer(many=True)
    category_name = CategorySerializer()
    class Meta:
        model = Item
        fields = '__all__'
