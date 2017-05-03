from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name= "index"),
    url(r'^process/(?P<route>\w+)$', views.process, name = "process"),
    url(r'^success$', views.success, name= "success"),
	url(r'^opinion$', views.opinion),
    # url(r'^create$', views.create, name = "create"),
]
