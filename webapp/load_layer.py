import os 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
from django.contrib.gis.utils import LayerMapping
from .models import annapurna

annapurna_mapping = {
    'objectid': 'OBJECTID',
    'dcode': 'DCODE',
    'district': 'DISTRICT',
    'dan': 'DAN',
    'das': 'DAS',
    'gapa_napa': 'GaPa_NaPa',
    'type_gn': 'Type_GN',
    'gn_code': 'GN_CODE',
    'new_ward_n': 'NEW_WARD_N',
    'ddgnww': 'DDGNWW',
    'center': 'CENTER',
    'state_code': 'STATE_CODE',
    'ddgn': 'DDGN',
    'area_sqkm': 'Area_SQKM',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
annapurna_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/annapurnawithward.shp'))
def run(verbose= True):
    lm=LayerMapping(annapurna, annapurna_shp, annapurna_mapping, transform= False, encoding= 'iso-8859-1')
    lm.save(strict=True,verbose=verbose)