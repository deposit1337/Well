from django.shortcuts import render, get_object_or_404
import sys

sys.path.append('D:/Well-ecommerce-api/main/')
from catalog.models import Item, Category
from .basket import Basket
from django.http import JsonResponse

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseBadRequest


# Create your views here.

def basket_summary(request):
    if request.method == 'POST':
        subtotal = int(request.POST.get('subtotal', 0))
        if subtotal <= 0:  # Проверка, что subtotal меньше или равен 0
            error_message = "Добавьте что-нибудь в корзину перед отправкой заявки."
            basket = Basket(request)
            return render(request, 'catalog/basket/summary.html', {'basket': basket, 'error_message': error_message})

        if 'fullname' in request.POST and 'email' in request.POST and 'phone' in request.POST and 'city' in request.POST:
            fullname = request.POST['fullname']
            email = request.POST['email']
            phone = request.POST['phone']
            city = request.POST['city']
            note = request.POST.get('note', '')

            basket = Basket(request)

            # Accessing session data
            session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)
            session_data = {}
            if session_key:
                session = SessionStore(session_key)
                session_data = session.load()

            # Prepare message including session data
            message = f"Name: {fullname}\nEmail: {email}\nPhone: {phone}\nCity: {city}\nNote: {note}\nSubtotal: {subtotal}\nSession Data: {session_data}"

            send_mail(
                'Subject of the Email',
                message,
                settings.EMAIL_HOST_USER,  # From email address
                [settings.EMAIL_HOST_USER],  # To email address
                fail_silently=False,
            )

            # Clear session data
            if session_key:
                session.delete()

            return HttpResponseRedirect(reverse('basket:basket_summary'))  # Redirect after form submission
    categories = Category.objects.all()
    basket = Basket(request)

    return render(request, 'catalog/basket/summary.html', {'basket': basket,'categories': categories,})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('itemid'))
        item_qty = int(request.POST.get('itemqty'))
        item = get_object_or_404(Item, id=item_id)

        basket.add(item, qty=item_qty)
        basketqty = basket.__len__()

        response = JsonResponse({
            'qty': basketqty
        })

        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'delete':
        item_id = int(request.POST.get('itemid'))
        basket.delete(item=item_id)
        baskettotal = basket.get_total_price()
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})

        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'update':
        item_id = int(request.POST.get('itemid'))
        item_qty = int(request.POST.get('itemqty'))
        basket.update(item=item_id, qty=item_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()

        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response



