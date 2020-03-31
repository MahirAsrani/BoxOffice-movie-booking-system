from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('register_cinema',views.register_cinema, name='register_cinema'),
    path('bookings',views.bookings, name='bookings'),
    path('profile',views.profile, name='profile'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('add_shows',views.add_shows, name='add_shows'),
    path('earnings',views.earnings, name='earnings'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)