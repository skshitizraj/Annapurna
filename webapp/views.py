from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.views.decorators import csrf
from django.contrib.gis.geos import Point, LineString, MultiLineString
from .models import annapurna,school
from django.http import HttpResponse
# from .forms import UploadGpxForm
from rest_framework import viewsets
from .serializers import annapurnaSerializer,schoolSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from django.conf import settings

def homepage(request):
    template_name= 'Home.html'
    return render(request,template_name)
def mappage(request):
    template_name= 'map.html'
    return render(request,template_name)
class annapurnaviewset(generics.ListAPIView):
    serializer_class=annapurnaSerializer
    def get_queryset(self):
        wardname= self.kwargs['wardno']
        if wardname != 'all':
            return annapurna.objects.filter(new_ward_n=wardname)
        else:
            return annapurna.objects.all()

class schoolviewset(generics.ListAPIView):
    # queryset = school.objects.all()
    serializer_class=schoolSerializer
    def get_queryset(self):
        wardname= self.kwargs['ward']
        newtype= self.kwargs['type']
        if wardname != 'all':
            if newtype!='all':
                # return school.objects.filter(school_location=wardname)
                return school.objects.filter(school_location=wardname,Type=newtype)
            return school.objects.filter(school_location=wardname)
        else:
            if newtype!='all':
                return school.objects.filter(Type=newtype)
            return school.objects.all()
      
        


