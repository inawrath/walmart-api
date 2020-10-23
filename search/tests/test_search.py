import pytest

from tests.conftest import mongo  # NOQA
from search.models import Product


@pytest.mark.usefixtures('mongo')
class TestSearch:
    def test_list(self):
        assert Product.objects.count() == 2

    def test_filter_by_test(self):
        list_products = Product.objects.search('rhr')
        assert list_products['total'] == 1

    def test_filter_by_id(self):
        list_products = Product.objects.search('1900')
        assert list_products['total'] == 1

    def test_filter_palindrome_search(self):
        list_products = Product.objects.search('lñl')
        assert list_products['products'][0]['has_discount'] is True
