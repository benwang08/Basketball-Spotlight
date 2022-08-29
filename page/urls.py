from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', LoginView.as_view(), name='NHp-login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('home/', views.home, name='NHp-home'),
    path('about/', views.about, name='NHp-about'),
    path('profile/', views.login, name='NHp-profile'),
    path('games', views.login, name='NHp-games'),
    path('news/', views.login, name='NHp-news'),


]
