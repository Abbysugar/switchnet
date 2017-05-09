from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'SwitchNet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("user_mgr.urls", namespace = "user_mgr")),
    url(r'^newsfeed/', include("newsfeed.urls", namespace = "newsfeed")),
    url(r'^messages/', include("messaging.urls", namespace = "messaging")),
]
