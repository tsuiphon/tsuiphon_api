from django.urls import path
from . import views

urlpatterns = [
    path('', views.top_page, name="top"),
    path('talk_page/', views.talk_page, name="talk_page"),
    path('room/', views.room),# TODO:あとで外す
]
