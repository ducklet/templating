from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^autoescape/$', views.autoescape, name='autoescape'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^csrf_token/$', views.csrf_token, name='csrf_token'),
    url(r'^cycle/$', views.cycle, name='cycle'),
    url(r'^debug/$', views.debug, name='debug'),
    url(r'^extends/$', views.extends, name='extends'),
]
