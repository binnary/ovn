"""ovn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from configovn.urls import *
admin.site.site_title = 'OVNAdmin'
admin.site.site_header = 'OpenVpn Admin'
admin.autodiscover()
urlpatterns = [
    url(r'doc/', include('django.contrib.admindocs.urls'), name='doc'),
    path(r'', admin.site.urls),
    #url(r'^contact/', include(configovn_urls)),
]
