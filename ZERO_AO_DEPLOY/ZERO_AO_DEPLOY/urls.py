from django.conf.urls import include, url
from django.contrib import admin
from core.views import HomeSiteView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',HomeSiteView.as_view(),name='home'),
]
