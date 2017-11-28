from apistar import typesystem


class ProductSerializer(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=100),
    }


class CartSerializer(typesystem.Object):
    properties = {
        'user': typesystem.string(max_length=100),
        'products': typesystem.array(),
        'vouchers': typesystem.array(),
        'coupons': typesystem.array(),
    }
