from django.conf.urls import url

from records import views

urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^(?P<record>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<record>\d+)/remove/$', views.remove, name='remove'),
    url(r'^(?P<record>\d+)/$', views.review, name='review'),
    url(r'^export/$', views.export_data, name='export'),
    url(r'^search/$', views.search, name='search'),
]
