from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class school(models.Model):
    SCHOOL_CHOICES =(
        ('Government','Government'),
        ('Private','Private'),
    )
    WARD_CHOICES =(
        ('wardno1','Ward No 1'),
        ('wardno2','Ward No 2'),
        ('wardno3','Ward No 3'),
        ('wardno4','Ward No 4'),
        ('wardno5','Ward No 5'),
        ('wardno6','Ward No 6'),
        ('wardno7','Ward No 7'),
        ('wardno8','Ward No 8'),
        ('wardno9','Ward No 9'),
        ('wardno10','Ward No 10'),
        ('wardno11','Ward No 11'),
    )
    STATUS_CHOICES=(
        ('updated','Updated'),
        ('notupdated','Not Updated'),
    )
    name = models.CharField(max_length=40)
    principal_name=models.CharField(max_length=40,blank=True)
    no_of_buildings=models.FloatField(blank=True,null=True)
    no_of_staffs= models.FloatField(blank=True,null=True)
    no_of_students= models.FloatField(blank=True,null=True)
    school_location= models.CharField(max_length=40,choices=WARD_CHOICES,null=True)
    status= models.CharField(max_length=20,choices=STATUS_CHOICES,default=STATUS_CHOICES[0][0],null=True)
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
    title= models.CharField(max_length=50)
    description= models.TextField(max_length=200)
    lat= models.FloatField()
    lon=models.FloatField()
    elevation=models.FloatField()
    # location= geomodels.PointField(srid=4326)


# def GPX_Folder(instance, filename):
#     return "uploaded_gpx_files/%s" % (filename)

# class gpxFile(models.Model):
#     title = models.CharField("Title", max_length=100)
#     gpx_file = models.FileField(upload_to=GPX_Folder, blank=True)

#     def __unicode__(self):
#         return self.title

# class GPXPoint(models.Model):
#     name = models.CharField("Name", max_length=50, blank=True)
#     description = models.CharField("Description", max_length=250, blank=True)
#     gpx_file = models.ForeignKey('gpxFile', on_delete=models.DO_NOTHING,)
#     point = geomodels.PointField()
#     # objects = models.GeoManager()
   
#     def __unicode__(self):
#         return unicode(self.name)
    

# class GPXTrack(models.Model):
#     track = geomodels.MultiLineStringField()
#     gpx_file = models.ForeignKey('gpxFile', on_delete=models.DO_NOTHING,)
#     # objects = models.GeoManager()
 