from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^package/', views.package, name='package'),
    url(r'^how/', views.how, name='how'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^client/', views.client, name='client'),
    url(r'^orders/', views.orders, name='orders'),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'Travel/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'Travel/logout.html'}, name='logout'),
]