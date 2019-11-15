from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.serializers import serialize
from django.views.decorators import csrf
from django.contrib.gis.geos import Point, LineString, MultiLineString
from .models import annapurna
from django.http import HttpResponse
# from .forms import UploadGpxForm
from rest_framework import viewsets
from .serializers import annapurnaSerializer
from django.contrib.auth.decorators import login_required

from django.conf import settings

# import gpxpy
# import gpxpy.gpx


# Create your views here.
def baseapi(request):
    base=serialize('geojson',annapurna.objects.all())
    return HttpResponse(base,content_type='json')
def homepage(request):
    template_name= 'Home.html'
    return render(request,template_name)
def mappage(request):
    template_name= 'map.html'
    return render(request,template_name)
# @login_required
class annapurnaviewset(viewsets.ModelViewSet):
    queryset = annapurna.objects.all().order_by('new_ward_n')
    serializer_class=annapurnaSerializer
    # return JsonResponse(serializer_class, safe=False)
    http_method_names = ['get', 'head','optionsc']
# def SaveGPXtoPostGIS(f, file_instance):
    
#     gpx_file = open(settings.MEDIA_ROOT+ '/uploaded_gpx_files'+'/' + f.name)
#     gpx = gpxpy.parse(gpx_file)

#     if gpx.waypoints:        
#         for waypoint in gpx.waypoints:            
#             new_waypoint = GPXPoint()
#             if waypoint.name:
#                 new_waypoint.name = waypoint.name
#             else:
#                 new_waypoint.name = 'unknown'
#             new_waypoint.point = Point(waypoint.longitude, waypoint.latitude)
#             new_waypoint.gpx_file = file_instance
#             new_waypoint.save()

#     if gpx.tracks:
#         for track in gpx.tracks:
#             print ("track name:" +str(track.name))
#             new_track = GPXTrack()
#             for segment in track.segments:
#                 track_list_of_points = []                
#                 for point in segment.points:
                    
#                     point_in_segment = Point(point.longitude, point.latitude)
#                     track_list_of_points.append(point_in_segment.coords)

#                 new_track_segment = LineString(track_list_of_points)
            
#             new_track.track = MultiLineString(new_track_segment)
#             new_track.gpx_file = file_instance    
#             new_track.save()


# def upload_gpx(request):
#     template_name='gpxupload.html'
#     args = {}
#     # args.update(csrf(request))

#     if request.method == 'POST':
#         file_instance = gpxFile()
#         form = UploadGpxForm(request.POST, request.FILES, instance=file_instance)
#         args['form'] = form
#         if form.is_valid():    
#             form.save()
#             SaveGPXtoPostGIS(request.FILES['gpx_file'], file_instance)

#             # return HttpResponseRedirect('success/')

#     else:
#         args['form'] = UploadGpxForm()

#     return render(request,template_name)

# def upload_success(request):
#     return render_to_response('webapp/success.html')
