import datetime

from mongoengine import Document, fields, connect


connect('snap_cart')


class Product(fields.EmbeddedDocument):
    name = fields.StringField(required=True, max_length=128)


class Voucher(fields.EmbeddedDocument):
    name = fields.StringField(required=True, max_length=128)


class Coupon(fields.EmbeddedDocument):
    name = fields.StringField(required=True, max_length=128)


class Cart(Document):
    slug = fields.StringField(required=True, max_length=128)
    user = fields.EmailField(max_length=128)
    products = fields.EmbeddedDocumentListField(Product)
    vouchers = fields.EmbeddedDocumentListField(Voucher)
    coupons = fields.EmbeddedDocumentListField(Coupon)

    date_updated = fields.DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'allow_inheritance': False
    }
