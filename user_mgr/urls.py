from django.conf.urls import url
from user_mgr import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^register/$', views.registerView, name='register'),
    url(r'^login/$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout'),
]
