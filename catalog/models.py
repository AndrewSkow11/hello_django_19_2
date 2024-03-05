from django.db import models
from django import forms

# Задание 2
# Добавьте новую модель «Версия», которая должна содержать следующие поля:
# продукт,
# номер версии,
# название версии,
# признак текущей версии.


# При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.
# Признак текущей версии — булево поле, является ли версия для продукта текущей для отображения на сайте или нет.
# Для отображения активной версии расширьте метод
# get_context_data()
#  контроллера списка продуктов, получите данные о версиях продукта и выберите текущую (активную) версию для продукта.
#




class Category(models.Model):
    nomination = models.CharField(max_length=150, verbose_name='наименование')
    description = models.CharField(max_length=150, verbose_name='описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.nomination} ({self.description})'

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
    price = models.DecimalField(decimal_places=3, max_digits=10)
    # Дата создания (записи в БД)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='дата создания')
    # Дата последнего изменения (записи в БД)
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='дата изменения')

    # manufactured_at
    manufactured_at = models.DateTimeField(null=True, blank=True,
                                           verbose_name='Дата производства продукта')

    def __str__(self):
        # Строковое отображение объекта
        return (f'{self.nomination} '
                f'{self.description} '
                f'{self.imagine_url} '
                f'{self.category} '
                f'{self.price} '
                f'{self.created_at} '
                f'{self.updated_at}'
                f'{self.manufactured_at}')

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    number = models.IntegerField(verbose_name='номер версии')
    nomination = models.CharField(max_length=50, verbose_name='название')
    is_current = models.BooleanField(default=True, verbose_name='текущая')


    def __str__(self):
        return f'{self.number}, ({self.nomination})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'