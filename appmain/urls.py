from django.urls import path

from appmain.views import create_item, show_main

app_name = 'appmain'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
]