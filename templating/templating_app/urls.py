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
    url(r'^filter/$', views.filter, name='filter'),
    url(r'^firstof/$', views.firstof, name='firstof'),
    url(r'^for/$', views.for_tag, name='for_tag'),
    url(r'^for_empty/$', views.for_empty, name='for_empty'),
    url(r'^if/$', views.if_tag, name='if_tag'),
    url(r'^ifchanged/$', views.ifchanged, name='ifchanged'),
    url(r'^include/$', views.include, name='include'),
    url(r'^load/$', views.load, name='load'),
    url(r'^lorem/$', views.lorem, name='lorem'),
    url(r'^now/$', views.now_tag, name='now_tag'),
    url(r'^regroup/$', views.regroup, name='regroup'),
    url(r'^spaceless/$', views.spaceless, name='spaceless'),
    url(r'^templatetag/$', views.templatetag, name='templatetag'),
]
