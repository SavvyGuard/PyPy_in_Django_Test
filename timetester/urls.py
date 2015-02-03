from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'test_json', views.test_json),
)
