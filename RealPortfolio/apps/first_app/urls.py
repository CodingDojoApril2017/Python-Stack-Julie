from django.conf.urls import url
from . import views           # So we can call functions from our routes!
urlpatterns = [
	url(r'^$', views.index),
    url(r'^about$', views.show),
    url(r'^projects$', views.projects),
    url(r'^testimonials$', views.testimonials)       # 'home' route.
]
