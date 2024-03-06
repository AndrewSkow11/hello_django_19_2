from django.core.management import BaseCommand
import json
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():

        categories_list = []

        with open("catalog_data.json") as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'catalog.category':
                categories_list.append(item)

        return categories_list

    @staticmethod
    def json_read_products():
        # Здесь мы получаем данные из фикстуры с продуктами

        products_list = []

        with open("catalog_data.json") as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'catalog.product':
                products_list.append(item)

        return products_list

    def handle(self, *args, **options):
        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры
        # для получения информации об одном объекте
        for category_item in Command.json_read_categories():
            category_for_create.append(
                Category(pk=category_item['pk'],
                         nomination=category_item['fields']['nomination'],
                         description=category_item['fields']['description'],
                         ))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(pk=product['pk'],
                        nomination=product['fields']['nomination'],
                        description=product['fields']['description'],
                        imagine_url=product['fields']['imagine_url'],
                        category=Category.objects.get(
                            pk=product['fields']['category']),
                        price=product['fields']['price'],
                        created_at=product['fields']['created_at'],
                        updated_at=product['fields']['updated_at'],
                        manufactured_at=product['fields']['manufactured_at']
                        ))

        Product.objects.bulk_create(product_for_create)
