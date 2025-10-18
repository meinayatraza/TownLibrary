from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('male/', views.book_list, {'section': 'male'}, name='male_section'),
    path('female/', views.book_list, {'section': 'female'}, name='female_section'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]