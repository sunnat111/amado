from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=100, unique=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"

class Brand(models.Model):
    title = models.CharField(verbose_name="Название бренда", max_length=100, unique=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

class Product(models.Model):
    title = models.CharField(verbose_name="Название товара", max_length=150, unique=True, default="")
    description = models.TextField(verbose_name="описание товара")
    price = models.IntegerField(verbose_name="Цена товара")
    quantity = models.IntegerField(verbose_name="Кол-во товара", default=10)
    is_available = models.BooleanField(default=True, verbose_name="В наличие")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(default="")

    def get_first_photo(self):
        try:
            photo = self.productimage_set.all()[0].photo.url
            return photo

        except Exception as e:
            return  "I am photo"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="products/", null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)