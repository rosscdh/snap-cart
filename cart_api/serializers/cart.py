from apistar import typesystem


class Product(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=100),
    }


class Cart(typesystem.Object):
    properties = {
        'user': typesystem.string(max_length=100),
        'products': typesystem.array(),
        'vouchers': typesystem.array(),
        'coupons': typesystem.array(),
    }
