from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls

from serializers.cart import Cart, Product


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


def detail_cart(cart):
    return {}


def add_product(cart, product):
    return {}

# def remove_product(cart, product):
#     return {}

# def update_product(cart, product):
#     return {}


def add_voucher(cart):
    return {}


def remove_voucher(cart, voucher):
    return {}


def update_voucher(cart, voucher):
    return {}


def add_promotion(cart):
    return {}


def remove_promotion(cart, promotion):
    return {}


def update_promotion(cart, promotion):
    return {}


routes = [
    Route('/', 'GET', welcome),
    Route('/cart/{cart}', 'GET', detail_cart),
    Route('/cart/{cart}', 'POST', add_product),
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

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
