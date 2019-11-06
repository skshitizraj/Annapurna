from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class school(models.Model):
    SCHOOL_CHOICES =(
        ('Government','Government'),
        ('Private','Private'),
    )
    name = models.CharField(max_length=40)
    location = geomodels.PointField(srid=4326)
    Type = models.CharField(max_length=40, blank=True)
class annapurna(models.Model):
    objectid = models.BigIntegerField()
    dcode = models.IntegerField()
    district = models.CharField(max_length=50)
    dan = models.CharField(max_length=50)
    das = models.IntegerField()
    gapa_napa = models.CharField(max_length=50)
    type_gn = models.CharField(max_length=50)
    gn_code = models.FloatField()
    new_ward_n = models.BigIntegerField()
    ddgnww = models.FloatField()
    center = models.CharField(max_length=50)
    state_code = models.IntegerField()
    ddgn = models.BigIntegerField()
    area_sqkm = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = geomodels.MultiPolygonField(srid=4326)
    class Meta:
        verbose_name_plural = "Annapurna"