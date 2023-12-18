"""
URL configuration for project24 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('topic_table/',topic_table,name='topic_table'),
    path('insert_into_topic/',insert_into_topic,name='insert_into_topic'),
    path('webpage/',webpage,name='webpage'),
    path('insert_into_webpage/',insert_into_webpage, name='insert_into_webpage'),
    path('accessrecord/',accessrecord,name='accessrecord'),
    path('insert_into_access/',insert_into_access,name='insert_into_access'),
]
