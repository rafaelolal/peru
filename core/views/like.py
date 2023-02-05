from django.http import JsonResponse

from ..models.place import Place

def like(request):
    place = Place.objects.get(pk=request.GET.get('place'))
    place.likes += 1
    place.save()
    data = {'likes': place.likes}
    return JsonResponse(data)