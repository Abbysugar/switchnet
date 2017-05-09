from django.conf.urls import url
from user_mgr import views

urlpatterns = [
    url(r'^$', views.IndexView, name='messaging'),
]
