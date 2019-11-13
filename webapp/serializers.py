# from rest_framework import serializers
from rest_framework_gis import serializers
from .models import annapurna

class annapurnaSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = annapurna
        geo_field='geom'
        fields = '__all__'