from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^autoescape/$', views.autoescape, name='autoescape'),
    url(r'^comment/$', views.comment, name='comment'),
]
