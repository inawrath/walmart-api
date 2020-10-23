import pytest
import mongoengine as me

from search.models import Product


list_products = [
    {
        "id_": "1881",
        "brand": "ooy eqrceli",
        "description": "rlñlw brhrka",
        "image": "www.lider.cl/catalogo/images/whiteLineIcon.svg",
        "price": "498724",
    },
    {
        "id_": "1900",
        "brand": "dsaasd",
        "description": "zlrwax bñyrh",
        "image": "www.lider.cl/catalogo/images/babyIcon.svg",
        "price": "130173",
    }
]


@pytest.fixture(scope='function')
def mongo(request):
    db = me.connect('testdb', host='mongomock://localhost')

    for product in list_products:
        db_product = Product(**product)
        db_product.save()

    yield db
    db.drop_database('testdb')
    db.close()
