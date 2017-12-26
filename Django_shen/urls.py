"""Django_shen URL Configuration

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
from cmdb import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
url(r'^index/', views.index),
url(r'^web_1/', views.web_1),
url(r'^$', views.web_blog),
url(r'^ie/', views.ie),
url(r'^base/', views.base),
url(r'^web_blog/content/(?P<pk>[0-9]+)/$', views.content,name="content"),
url(r'^web_blog/data/$', views.data),
]
