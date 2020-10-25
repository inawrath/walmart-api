from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Product


class SearchApiView(View):

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        text = request.GET.get('text', '').strip()
        page = request.GET.get('page', '1')
        page = int(page) if page.isnumeric() else 1

        return JsonResponse(data=Product.objects.search(text, page), safe=False)
