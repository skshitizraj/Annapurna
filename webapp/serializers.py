# from rest_framework import serializers
from rest_framework_gis import serializers
from .models import annapurna,school

class annapurnaSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = annapurna
        geo_field='geom'
        fields = '__all__'
        
class schoolSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = school
        geo_field='location'
        fields = '__all__'