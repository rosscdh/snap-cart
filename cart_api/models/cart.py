import datetime

from mongoengine import Document, fields, connect


connect('snap_cart')


class Cart(Document):
    user = fields.EmailField(required=True, max_length=200)
    products = fields.EmbeddedDocumentListField(fields.EmbeddedDocument())
    vouchers = fields.EmbeddedDocumentListField(fields.EmbeddedDocument())
    coupons = fields.EmbeddedDocumentListField(fields.EmbeddedDocument())

    date_created = fields.DateTimeField(default=datetime.datetime.utcnow)
    date_updatd = fields.DateTimeField(default=datetime.datetime.utcnow)

    meta = {
        'allow_inheritance': False
    }
