from django.conf.urls import url,include
from django.urls import path
from rest_framework import routers
from .import views

# router = routers.DefaultRouter()
# router.register(r'annapurna', views.annapurnaviewset)
urlpatterns = [
    path('baseapi/', views.baseapi,name='Geojsonbase'),
    path('',views.homepage,name='home'),
    path('map/',views.mappage,name='map'),
    # path('gpxupload/',views.upload_gpx,name='gpx'),
    # path('api/', include(router.urls)),
    path('api/ward/<slug:wardno>/',views.annapurnaviewset.as_view()),
    # path('baseapi/ward/')
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
  

]