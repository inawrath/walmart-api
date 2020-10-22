from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Products


class SearchApiView(View):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        products = Products.objects.all()

        return JsonResponse(data=[product.to_dictionary() for product in products], safe=False)
