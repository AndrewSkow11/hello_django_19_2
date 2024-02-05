from django.db import models


class Category(models.Model):
    nomination = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.nomination} {self.description}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    # Наименование
    nomination = models.CharField(max_length=150, verbose_name='наименование')
    # Описание
    description = models.TextField(verbose_name='описание')
    # Изображение (превью)
    imagine_url = models.ImageField(upload_to='products/',
                                    verbose_name='изображение',
                                    null=True, blank=True)
    # Категория
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Цена за покупку
    price = models.DecimalField()
    # Дата создания (записи в БД)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='дата создания')
    # Дата последнего изменения (записи в БД)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='дата изменения')

    def __str__(self):
        # Строковое отображение объекта
        return (f'{self.nomination} '
                f'{self.description} '
                f'{self.imagine_url} '
                f'{self.category} '
                f'{self.price} '
                f'{self.created_at} '
                f'{self.updated_at}')

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов
