from rest_framework import serializers
from .models import annapurna

class annapurnaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = annapurna
        fields = '__all__'