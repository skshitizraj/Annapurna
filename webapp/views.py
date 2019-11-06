from django.shortcuts import render
from django.core.serializers import serialize
from .models import annapurna
from django.http import HttpResponse


# Create your views here.
def baseapi(request):
    base=serialize('geojson',annapurna.objects.all())
    return HttpResponse(base,content_type='json')