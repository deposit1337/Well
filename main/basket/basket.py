import sys

sys.path.append('D:/Well-ecommerce-api/main/')
from catalog.models import Item


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, item, qty):
        item_id = str(item.id)

        if item_id in self.basket:
            self.basket[item_id]['qty'] = qty
        else:
            self.basket[item_id] = {'price': item.price, 'qty': qty}

        self.session.pop('_auth_user_id', None)
        self.session.pop('_auth_user_backend', None)
        self.session.pop('_auth_user_hash', None)

        self.session.modified = True

    def __iter__(self):
        item_ids = self.basket.keys()
        items = Item.items.filter(id__in=item_ids)
        basket = self.basket.copy()

        for item in items:
            basket[str(item.id)]['item'] = item

        for thing in basket.values():
            thing['price'] = int(thing['price'])
            thing['total_price'] = thing['price'] * thing['qty']
            yield thing

    def __len__(self):
        '''
        Get basket data and count qty of items
        '''
        return sum(item['qty'] for item in self.basket.values())

    def get_total_price(self):
        return sum(thing['price'] * int(thing['qty']) for thing in self.basket.values())

    def delete(self, item):
        item_id = str(item)
        if item_id in self.basket:
            del self.basket[item_id]

        self.session.modified = True  # Make a save function in the future

    def update(self, item, qty):
        item_id = str(item)
        if item_id in self.basket:
            self.basket[item_id]['qty'] = qty

        self.session.modified = True
