from django.db import models
from django.urls import reverse

# Create your models here.
class ItemManager(models.Manager):
    def get_queryset(self):
        return super(ItemManager, self).get_queryset().filter(is_active=True)


class Brand(models.Model):
    brand = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brand


class Category(models.Model):
    category_name = models.CharField(max_length=100, default=None, null=True)
    category_picture = models.ImageField(upload_to='images/category-images/', default=None, null=True)
    broad_name = models.CharField(max_length=100, default=None, null=True)
    slug = models.SlugField(max_length=255, default=None, null=True)
    whatfor1 = models.CharField(max_length=100 ,default=None, null=True)
    whatfor2 = models.CharField(max_length=100 ,default=None,null=True)
    whatfor1_num = models.CharField(max_length=100 ,default=None,null=True )
    whatfor2_num = models.CharField(max_length=100 ,default=None,null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class AdditionalPicture(models.Model):
    picture = models.ImageField(upload_to='images/additional_images/')

    def __str__(self):
        return self.picture.name.split('/')[-1]

    class Meta:
        verbose_name = 'Дополнительное фото'
        verbose_name_plural = 'Дополнительные фото'

class Accessory(models.Model):
    name = models.CharField(max_length=100)  # Название комплектующего

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состав'
        verbose_name_plural = 'Состав'


class Item(models.Model):
    full_name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    vendor = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    main_picture = models.ImageField(upload_to='images/')
    additional_pic = models.ManyToManyField(AdditionalPicture)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True)
    slug = models.SlugField(max_length=255, default=None, null=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    price = models.IntegerField(default=None, null=True)
    accessories = models.ManyToManyField(Accessory, blank=True)  # Поле для комплектующих
    updated_at = models.DateTimeField(auto_now=True)


    objects = models.Manager()
    items = ItemManager()

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('item_detail', args=[self.category_name.slug, self.id])
