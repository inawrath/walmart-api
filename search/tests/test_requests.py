import pytest

from django.test import Client

from tests.conftest import mongo  # NOQA


@pytest.mark.usefixtures('mongo')
class TestRequests:
    def test_list_products(self):
        test_client = Client()

        response = test_client.get('/search')
        assert len(response.json()['products']) == 2

    def test_second_page(self):
        test_client = Client()
        response = test_client.get('/search', {'page': 2})
        assert len(response.json()['products']) == 0
