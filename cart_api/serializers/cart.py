from apistar import typesystem

from commands.sign_product import sign_product


class ProductSerializer(typesystem.Object):
    properties = {
        'name': typesystem.string(max_length=100),
        'agreed_price': typesystem.integer(),
        'signature': typesystem.string(max_length=255),
    }

    def is_valid(self, valid_signature) -> bool:
        return valid_signature == self.signature


class CartSerializer(typesystem.Object):
    properties = {
        'user': typesystem.string(max_length=100),
        'products': typesystem.array(),
        'vouchers': typesystem.array(),
        'coupons': typesystem.array(),
    }
