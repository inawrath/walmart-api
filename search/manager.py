from mongoengine.queryset import QuerySet
from mongoengine.queryset.visitor import Q

from helpers import text_palindrome

ITEMS_PER_PAGE = 12


class ProductManager(QuerySet):

    def search(self, search, page=1):
        is_palindrome = text_palindrome(search)
        filter_query = Q()

        if search.isnumeric():
            filter_query = Q(id_=search)
        else:
            if len(search) > 3:
                filter_query = Q(brand__contains=search) | Q(description__contains=search)
        query = self.filter(filter_query)

        total = query.count()
        products = query[ITEMS_PER_PAGE * (page - 1):ITEMS_PER_PAGE * page]

        return dict(
            products=[product.transform_product(is_palindrome) for product in products],
            total=total,
            page=page,
            total_pages=(total // ITEMS_PER_PAGE) + (1 if total % ITEMS_PER_PAGE > 0 else 0),
        )
