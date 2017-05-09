from django.conf.urls import url
from newsfeed import views

urlpatterns = [

    #url(r'^$', views.IndexView, name='index'),
    url(r'^(?P<username>[\w]+)/$', views.newsfeedView, name="user_newsfeed"),

]
