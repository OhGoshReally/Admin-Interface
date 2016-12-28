from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logs/', views.logs, name='logs'),
    url(r'^statustest/', views.statustest, name='statustest'),
    url(r'^settings/', views.settings, name='settings'),
    url(r'^login/', views.loginView, name='login'),
    url(r'^logout/', views.logoutView, name='logout'),
    url(r'^status/', views.statustest, name='status'),
    url(r'^api', views.api, name='api'),
]
