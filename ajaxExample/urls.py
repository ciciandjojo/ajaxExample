"""ajaxExample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import ajax.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_list/$', ajax.views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', ajax.views.ajax_dict, name='ajax-dict'),
    url(r'^ajax_jquery/$', ajax.views.ajax_jquery, name='ajax-jquery'),
    url(r'^ajax_jquery_POST/$', ajax.views.ajax_jquery_POST,
        name='ajax-jquery-POST'),
    url(r'^ajax_jquery_sample/$', ajax.views.ajax_jquery_sample,
        name='ajax-jquery-sample'),
    url(r'^index/$', ajax.views.index, name='index'),
]
