from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='landing_page'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-trip/', views.create_trip, name='create-trip')
]