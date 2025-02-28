from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import Http404
import sys
from .models import Item, Brand, AdditionalPicture, Category
from .serializers import ItemSerializer, CategorySerializer, BrandSerializer, AdditionalPictureSerializer

sys.path.append('D:/Well-ecommerce-api/main/')
from drf_spectacular.utils import extend_schema

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse


class ItemView(viewsets.ViewSet):
    # Class based viewset to all items

    queryset = Item.objects.all()

    @extend_schema(responses=ItemSerializer)
    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)


class CategoryView(viewsets.ViewSet):
    # Class based viewset to all categories

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


def home_page(request):
    categories = Category.objects.all()
    first_three_categories = categories[:3]
    next_three_categories = categories[3:6]
    return render(request, 'catalog/index.html', {
        'first_three_categories': first_three_categories,
        'next_three_categories': next_three_categories,
        'categories': categories  # Передаем все категории
    })


# def catalog(request, category_slug):
#     category = Category.objects.get(slug=category_slug)
#     items = Item.objects.filter(category_name=category)
#     cart_data = request.session.get('skey', {})
#     return render(request, 'catalog/catalog.html', {'category': category, 'items': items, 'cart_data': cart_data})

def catalog(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    items = Item.objects.filter(category_name=category)
    cart_data = request.session.get('skey', {})

    # Разделение элементов на две группы по три элемента
    first_three_items = items[:3]
    next_three_items = items[3:6]

    return render(request, 'catalog/catalog.html', {
        'category': category,
        'first_three_items': first_three_items,
        'next_three_items': next_three_items,
        'cart_data': cart_data,
        'categories': categories,

    })


def item_detail(request, category_slug, item_id):
    item = get_object_or_404(Item, id=item_id)
    category = get_object_or_404(Category, slug=category_slug)  # Получаем категорию по slug
    categories = Category.objects.all()

    # Передаем дополнительные изображения вместе с другими данными
    return render(request, 'catalog/item-of-category.html', {
        'category_slug': category_slug,
        'category': category,  # Передаем категорию для навигации
        'item': item,
        'categories': categories,
    })


def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        item = get_object_or_404(Item, vendor=searched)
        return redirect('item_detail', category_slug=item.category_name.slug, item_id=item.id)
    else:
        raise Http404("Страница не найдена")




from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings



def custom_404_view(request, exception=None):
    categories = Category.objects.all()

    if request.method == 'POST':
        try:
            # Получаем данные из формы
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            city = request.POST.get('city')
            note = request.POST.get('note')


            if not fullname or not email or not phone:

                return render(request, '404.html', {
                    'categories': categories,
                    'error_message': 'Пожалуйста, заполните все обязательные поля.'
                }, status=400)


            message = f"""
            ФИО: {fullname}
            Email: {email}
            Телефон: {phone}
            Город: {city}
            Запрос: {note}
            """

            # Отправляем письмо
            send_mail(
                'Новая заявка с сайта',  # Тема письма
                message,  # Тело письма
                settings.EMAIL_HOST_USER,  # Отправитель (ваш email)
                [settings.EMAIL_HOST_USER],  # Получатель
                fail_silently=False,
            )


            return redirect('home_page')

        except Exception as e:

            print(f"Произошла ошибка при отправке формы: {e}")
            return render(request, '404.html', {
                'categories': categories,
                'error_message': 'Произошла ошибка при отправке формы. Пожалуйста, попробуйте ещё раз.'
            }, status=500)


    return render(request, '404.html', {'categories': categories}, status=404)


def custom_500_view(request):
    return render(request, '500.html', status=500)

#
# def test_404(request):
#     categories = Category.objects.all()
#     return render(request, '404.html', {'categories': categories})


# def ticket_form(request):
