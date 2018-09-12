from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^/$', views.index, name='index'),
    url(r'^/(?P<upload_id>[0-9]+)/$', views.detail, name='detail')
]
