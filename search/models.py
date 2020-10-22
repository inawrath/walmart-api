from bson.objectid import ObjectId
from decimal import Decimal
from mongoengine import (
    Document,
    StringField,
    LongField,
)

from .manager import ProductManager


class Products(Document):
    id_ = LongField(unique=True, db_field="id")
    brand = StringField()
    description = StringField()
    image = StringField()
    price = LongField()

    meta = {
        'queryset_class': ProductManager,
    }

    def to_dictionary(self):
        dictionary = {}
        for a in self:
            attr = getattr(self, a)
            if type(attr) in [str, int, float]:
                dictionary[a] = attr
            elif type(attr) is Decimal:
                dictionary[a] = float(attr)
            elif type(attr) is ObjectId:
                dictionary[a] = str(attr)
        return dictionary

    def transform_product(self, is_palindrome):
        temp_product = self.to_dictionary()
        temp_product['has_discount'] = is_palindrome
        temp_product['price_discount'] = temp_product['price'] * 0.5 if is_palindrome else 0
        return temp_product
