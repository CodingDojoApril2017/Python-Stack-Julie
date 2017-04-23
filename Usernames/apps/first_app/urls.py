from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
    url(r'^create$', views.create, name ="create"),
    url(r'^success$', views.success, name ="success")
]
