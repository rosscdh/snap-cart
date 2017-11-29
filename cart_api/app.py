import json
from apistar import Command, Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls

from commands.sign_product import (sign_product,
                                   unsign_product)

from models.cart import (Cart,
                         Product)

from serializers.cart import (CartSerializer,
                              ProductSerializer)

def _create_empty_cart(slug: str) -> Cart:
    return Cart(slug=slug)


def _cart_by_slug(slug: str) -> Cart:
    cart = Cart.objects.filter(slug=slug).first() or _create_empty_cart(slug=slug)
    if not cart.pk:
        # uff not good
        cart.save()
    return cart


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def products():
    products = json.load(open('../fixtures/products.json'))
    return [ProductSerializer(product) for product in products]


def detail_cart(id: str):
    cart = _cart_by_slug(slug=id)
    cart_serializer = CartSerializer({
        'user': cart.user,
        'products': [ProductSerializer(product._data) for product in cart.products],
        'vouchers': [],
        'coupons': [],
    })
    return cart_serializer


def modify_cart(id: str, data: CartSerializer):
    """
    """
    cart = _cart_by_slug(slug=id)

    cart.user = data.get('user')

    cart.products = [Product(**product) for product in data.get('products', [])]
    # cart.vouchers       = data.get('vouchers', [])
    # cart.coupons        = data.get('coupons', [])
    cart.save()

    return data


def remove_cart(id: str):
    cart = _cart_by_slug(slug=id)
    cart.delete()
    return {}


def add_product(id: str, data: ProductSerializer):
    cart = _cart_by_slug(slug=id)
    product = Product(**data)

    cart.products.append(product)
    cart.save()

    cart_serializer = CartSerializer({
        'user': cart.user,
        'products': [ProductSerializer(product._data) for product in cart.products],
        'vouchers': [],
        'coupons': [],
    })
    return cart_serializer

# def remove_product(cart, product):
#     return {}

# def update_product(cart, product):
#     return {}


# def add_voucher(id):
#     return {}


# def remove_voucher(id: str, cart: CartSerializer):
#     return {}


# def update_voucher(id: str, cart: CartSerializer, voucher: VoucherSerializer):
#     return {}


# def add_promotion(cart):
#     return {}


# def remove_promotion(cart, promotion):
#     return {}


# def update_promotion(cart, promotion):
#     return {}


def done(id: str):
    cart = _cart_by_slug(slug=id)
    #
    # Send info to 3rd party systems
    # perform log of done event via email/log/influxdb
    # trigger other relevant events
    #
    return {}


routes = [
    Route('/', 'GET', welcome),
    # example products
    Route('/products', 'GET', products),

    Route('/cart/{id}', 'GET', detail_cart),
    Route('/cart/{id}', 'POST', modify_cart),
    Route('/cart/{id}', 'DELETE', remove_cart),
    Route('/cart/{id}/products', 'POST', add_product),

    Route('/cart/{id}/done', 'POST', done),
    # Route('/cart/{cart}/products/{product}', 'DELETE', remove_product),
    # Route('/cart/{cart}/products/{product}', 'PUT', update_product),

    # Route('/cart/{cart}/vouchers', 'POST', add_voucher),
    # Route('/cart/{cart}/vouchers/{voucher}', 'DELETE', remove_voucher),
    # Route('/cart/{cart}/vouchers/{voucher}', 'PUT', update_voucher),

    # Route('/cart/{cart}/promotion', 'POST', add_promotion),
    # Route('/cart/{cart}/promotion/{promotion}', 'DELETE', remove_promotion),
    # Route('/cart/{cart}/promotion/{promotion}', 'PUT', update_promotion),

    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

commands = [
    Command('sign_product', sign_product),
    Command('unsign_product', unsign_product),
]

app = App(routes=routes,
          commands=commands)


if __name__ == '__main__':
    app.main()
