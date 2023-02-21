from django.db import models

# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    description = models.CharField(max_length=100, null=True, blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")

    def __str__(self):
        return f"{self.title} - {self.description}"


class Products(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name="Описание")
    category = models.ForeignKey(to='Categories',
                                verbose_name='Категории',
                                related_name='category',
                                on_delete=models.RESTRICT)
    price = models.DecimalField(max_digits=6,  decimal_places=2)
    image = models.CharField(max_length=100, null=False, blank=False, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")

    def __str__(self):
        return f"{self.description} - {self.price}"
