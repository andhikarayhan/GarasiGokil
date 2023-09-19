from django.urls import path

from appmain.views import show_main

app_name = 'appmain'

urlpatterns = [
    path('', show_main, name='show_main'),
]