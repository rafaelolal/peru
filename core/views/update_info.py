from django.http import JsonResponse
from django.urls import reverse_lazy

from ..models.page import Page

def update_info(request):
    period = request.GET.get('period', 'Incas')
    category = request.GET.get('category', 'Historia')
    page = Page.objects.get(period=period, category=category)

    data = {
        'period': page.period,
        'category': page.category,
        'map': f"{page.map.url}",
        'section': f"{reverse_lazy('core:section_create', kwargs={'page_pk': page.pk})}",
        'place': f"{reverse_lazy('core:place_create', kwargs={'page_pk': page.pk})}",
        'update': f"{reverse_lazy('core:page_update', kwargs={'pk': page.pk})}",
        
        'sections': [page.sections.count(),
            [(section.title,
              reverse_lazy('core:section_update', kwargs={'pk': section.pk, 'page_pk': page.pk}),
              section.content,
              section.image.url) for section in page.sections.order_by('order')]],
        
        'places': [page.places.count(),
            [(place.name,
              reverse_lazy('core:place_update', kwargs={'pk': place.pk, 'page_pk': page.pk}),
              place.description,
              place.image.url,
              place.pk,
              place.likes) for place in page.places.all()]],
              
    }

    return JsonResponse(data)