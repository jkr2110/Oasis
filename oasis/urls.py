from django.conf.urls import patterns, url

from oasis import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fooddesert.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^map/$', views.map, name='map'),
    url(r'^grocery/$', views.grocery, name='grocery'),
    url(r'^restaurant/$', views.restaurant, name='restaurant'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
)
