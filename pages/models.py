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