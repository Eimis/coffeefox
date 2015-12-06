from django.conf.urls import include, url
from django.contrib import admin

from coffeefox.views import landing


urlpatterns = [
    url(r'^$', landing, name='landing'),
    url(r'^admin/', include(admin.site.urls)),
]
