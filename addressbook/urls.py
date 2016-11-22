from django.conf.urls import url, include
from django.conf.urls.static import static
from addressbook import settings
from django.contrib import admin

from addressbook import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^records/', include('records.urls')),
    url(r'^$', views.main, name='main'),
] #\
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
