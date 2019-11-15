from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class school(models.Model):
    SCHOOL_CHOICES =(
        ('Government','Government'),
        ('Private','Private'),
    )
    # WARD_CHOICES =(
    #     ('wardno1','Ward 1'),
    #     ('wardno2','Ward 2'),
    #     ('wardno3','Ward 3'),
    #     ('wardno4','Ward 4'),
    #     ('wardno5','Ward 5'),
    #     ('wardno6','Ward 6'),
    #     ('wardno7','Ward 7'),
    #     ('wardno8','Ward 8'),
    #     ('wardno9','Ward 9'),
    #     ('wardno10','Ward 10'),
    #     ('wardno11','Ward 11'),
    # )
    name = models.CharField(max_length=40)
    # principal_name=models.CharField(max_length=40)
    # no_of_buildings=models.FloatField()
    # no_of_staffs= models.FloatField()
    # no_of_students= models.FloatField()
    location = geomodels.PointField(srid=4326)
    Type = models.CharField(max_length=40,choices=SCHOOL_CHOICES)
   
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
def GPX_Folder(instance, filename):
    return "uploaded_gpx_files/%s" % (filename)

class gpxFile(models.Model):
    title = models.CharField("Title", max_length=100)
    gpx_file = models.FileField(upload_to=GPX_Folder, blank=True)

    def __unicode__(self):
        return self.title

class GPXPoint(models.Model):
    name = models.CharField("Name", max_length=50, blank=True)
    description = models.CharField("Description", max_length=250, blank=True)
    gpx_file = models.ForeignKey('gpxFile', on_delete=models.DO_NOTHING,)
    point = geomodels.PointField()
    # objects = models.GeoManager()
   
    def __unicode__(self):
        return unicode(self.name)
    

class GPXTrack(models.Model):
    track = geomodels.MultiLineStringField()
    gpx_file = models.ForeignKey('gpxFile', on_delete=models.DO_NOTHING,)
    # objects = models.GeoManager()
 