from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('top/', views.top_page, name="top"),
    path('talk_page/', views.talk_page, name="talk_page"),
    path('login/', LoginView.as_view(template_name='login.html')),
    path('logout/', LogoutView.as_view(template_name='logout.html')),
]
