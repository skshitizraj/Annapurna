from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from .models import school,annapurna,gpx
from leaflet.admin import LeafletGeoAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class SchoolResource(resources.ModelResource):
    class Meta:
        model = school

class schooladmin(LeafletGeoAdmin,ImportExportModelAdmin):
    resource_class = SchoolResource
    list_display=('name','Type','school_location')
    settings_overrides =  {
        'DEFAULT_CENTER': (28.333, 84.000),
        'DEFAULT_ZOOM': 12,
        'MIN_ZOOM': 5,  
        'MAX_ZOOM': 24,
        'TILES': [('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }
class annapurnaadmin(LeafletGeoAdmin):
    
    list_display=('new_ward_n','gapa_napa')
    ordering = ('new_ward_n',)
    settings_overrides =  {
        # 'DEFAULT_CENTER': (28.333, 84.000),
        'DEFAULT_ZOOM': 12,
        'MIN_ZOOM': 5,
        'MAX_ZOOM': 24,
        'TILES': [('Google Streets','http://mt0.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',''),('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }
class gpxadmin(LeafletGeoAdmin):
    
    list_display=('title','description')
    # ordering = ('new_ward_n',)
    settings_overrides =  {
        'DEFAULT_CENTER': (28.333, 84.000),
        'DEFAULT_ZOOM': 12,
        'MIN_ZOOM': 5,  
        'MAX_ZOOM': 24,
        'TILES': [('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }

admin.site.register(annapurna,annapurnaadmin)

admin.site.register(school,schooladmin)
admin.site.register(gpx,gpxadmin)
# geoadmin.site.register(GPXPoint, geoadmin.OSMGeoAdmin)
# geoadmin.site.register(GPXTrack, geoadmin.OSMGeoAdmin)
# admin.site.register(gpxFile)