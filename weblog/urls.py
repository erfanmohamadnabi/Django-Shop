from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('weblog',Weblog,name='weblog'),
    path('weblog/category/<cat>',Weblog_Category,name='weblog_category'),
    path('weblog/<pk>/<slug>',Detail_Weblog,name='detail_weblog'),
]