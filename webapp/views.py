from django.shortcuts import render
from django.core.serializers import serialize
from .models import annapurna
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import annapurnaSerializer
from django.contrib.auth.decorators import login_required


# Create your views here.
def baseapi(request):
    base=serialize('geojson',annapurna.objects.all())
    return HttpResponse(base,content_type='json')
def homepage(request):
    template_name= 'home.html'
    return render(request,template_name)
# @login_required
class annapurnaviewset(viewsets.ModelViewSet):
    queryset = annapurna.objects.all().order_by('new_ward_n')
    serializer_class=annapurnaSerializer
