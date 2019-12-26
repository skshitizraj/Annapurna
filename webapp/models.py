from django.db import models
from django.contrib.gis.db import models as geomodels
from django.contrib.gis.geos import Point
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.geos import GEOSGeometry


# Create your models here.

class school(models.Model):
    SCHOOL_CHOICES =(
        ('Government','Government'),
        ('Private','Private'),
    )
    WARD_CHOICES =(
        ('1','Ward No 1'),
        ('2','Ward No 2'),
        ('3','Ward No 3'),
        ('4','Ward No 4'),
        ('5','Ward No 5'),
        ('6','Ward No 6'),
        ('7','Ward No 7'),
        ('8','Ward No 8'),
        ('9','Ward No 9'),
        ('10','Ward No 10'),
        ('11','Ward No 11'),
    )
    STATUS_CHOICES=(
        ('updated','Updated'),
        ('notupdated','Not Updated'),
    )
    name = models.CharField(max_length=100,default='Null')
    principal_name=models.CharField(max_length=80,blank=True)
    no_of_buildings=models.FloatField(blank=True,null=True)
    no_of_staffs= models.FloatField(blank=True,null=True)
    no_of_students= models.FloatField(blank=True,null=True)
    school_location= models.CharField(max_length=100,choices=WARD_CHOICES,null=True)
    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_CHOICES[1][1],null=True)
    contact=models.CharField(max_length=10,blank=True,null=True)
    location = geomodels.PointField(srid=4326,null=True)
    Type = models.CharField(max_length=40,choices=SCHOOL_CHOICES,blank=True)
   
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

class gpx(models.Model):
    GPX_CHOICES =(
        ('School','School'),
        ('Annapurna','Annapurna'),
    )
    title= models.CharField(max_length=50)
    description= models.TextField(max_length=200)
    lat= models.FloatField()
    lon=models.FloatField()
    elevation=models.FloatField()
    field= models.CharField(max_length=40,choices=GPX_CHOICES,null=True)

@receiver(post_save, sender=gpx)
def make_author(sender, instance, created, **kwargs):
    
    if instance.field=='School':
        school.objects.create(name=instance.title,location=Point(instance.lon, instance.lat))
        # school.objects.create(location=GEOSGeometry('POINT(%f %f)' % (instance.lat, instance.lon)))
        
        
    # location= geomodels.PointField(srid=4326)
