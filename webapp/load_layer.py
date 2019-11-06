import os 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
from django.contrib.gis.utils import LayerMapping
from .models import annapurna

annapurna_mapping = {
    'objectid_1': 'OBJECTID_1',
    'objectid': 'OBJECTID',
    'palika': 'PALIKA',
    'district': 'DISTRICT',
    'gapa_napa': 'GAPA_NAPA',
    'gn_type': 'GN_TYPE',
    'province': 'PROVINCE',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
annapurna_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/annapurnawithward.shp'))
def run(verbose= True):
    lm=LayerMapping(annapurna, annapurna_shp, annapurna_mapping, transform= False, encoding= 'iso-8859-1')
    lm.save(strict=True,verbose=verbose)