from apistar import typesystem

from commands.sign_product import sign_product


class ProductSerializer(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=100),
        'agreed_price': typesystem.integer(),
        'signature': typesystem.string(max_length=255),
    }


class CartSerializer(typesystem.Object):
    properties = {
        'user': typesystem.string(max_length=100),
        'products': typesystem.array(items=[ProductSerializer], min_items=0),
        'vouchers': typesystem.array(min_items=0, unique_items=True),
        'coupons': typesystem.array(min_items=0, unique_items=True),
    }
