from django.db import models

class ProductCategory(models.Model):
    objects = None
    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category'

class Product(models.Model):
    objects = None
    object = None
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="category")
    name = models.CharField(verbose_name='product name', max_length=128)
    short_desk = models.CharField(max_length=256,blank=True, verbose_name='short dicription')
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.CharField(max_length=256,blank=True, verbose_name='dicription')
    price = models.DecimalField(verbose_name='price', max_digits=8, decimal_places=2, default=0)
    quanity = models.PositiveIntegerField(verbose_name='quanity', default=0)

    def __str__(self):
        return f'{self.name} - {self.pk}'

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
