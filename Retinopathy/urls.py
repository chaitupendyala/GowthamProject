from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^check$',views.enter_image),
    url(r'^store$',views.store_image),
]
