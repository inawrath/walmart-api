from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Products


class SearchApiView(View):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        search = request.GET.get('search', '').strip()
        page = request.GET.get('page', '1')
        page = int(page) if page.isnumeric() else 1

        return JsonResponse(data=Products.objects.search(search, page), safe=False)
