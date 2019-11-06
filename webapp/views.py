from django.shortcuts import render
from django.core.serializers import serialize
from .models import annapurna
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import annapurnaSerializer


# Create your views here.
def baseapi(request):
    base=serialize('geojson',annapurna.objects.all())
    return HttpResponse(base,content_type='json')
class annapurnaviewset(viewsets.ModelViewSet):
    queryset = annapurna.objects.all().order_by('new_ward_n')
    serializer_class=annapurnaSerializer