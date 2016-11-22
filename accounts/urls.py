from django.conf.urls import url
from django.contrib.auth.views import login, logout

from accounts import views

urlpatterns = [
    # url(r'^login/', account_login, name='login'),
    # url(r'^logout/', account_logout, name='logout'),
    url(r'^login/', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/', logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^register/', views.register, name='register'),
]
