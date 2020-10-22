from mongoengine import *
from bson.objectid import ObjectId
from decimal import Decimal


def serializer_mdb(self):
    dictionary = {}
    for a in self:
        attr = getattr(self, a)
        if type(attr) in [str, int, float]:
            dictionary[a] = attr
        elif type(attr) is Decimal:
            dictionary[a] = float(attr)
        elif type(attr) is ObjectId:
            dictionary[a] = str(attr)
        elif attr is not None:
            dictionary[a] = attr.to_dictionary()
    return dictionary


class Products(Document):

    brand = StringField()
    description = StringField()
    image = StringField()
    price = LongField()

    def to_dictionary(self):
        return serializer_mdb(self)
