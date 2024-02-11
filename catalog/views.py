from django.shortcuts import render
from catalog.models import Product


# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе,
        # который отправлял пользователь
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # а также передается информация, которую заполнил пользователь
        print("Сбор информации юзера (передача в консоль)")
        print(name)
        print(phone)
        print(message)

    return render(request, 'catalog/contacts.html')

def product(request, pk):

    context = {'object': Product.objects.get(pk=pk)}

    return render(request, 'catalog/products.html', context=context)

