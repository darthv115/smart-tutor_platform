from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^do/', views.sms, name='sms'),
    url(r'^sent/', views.sent, name='sent'),
]