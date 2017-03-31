from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^test$', views.test, name='test'),
    url(r'^profile$', views.profile, name='profile'),
]