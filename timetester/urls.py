from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'test_blank', views.test_blank),
    url(r'test_json', views.test_json),
    url(r'test_openrtb', views.test_openrtb),
    url(r'test_uuid', views.test_uuid),
    url(r'test_geoip', views.test_geoip),
    url(r'test_kafka', views.test_kafka),
)
