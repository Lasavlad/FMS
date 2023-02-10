from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.index, name='landing_page'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-trip/', views.create_trip, name='create-trip'),
    path('update_trip/<int:id>/', views.update_trip, name='update-trip'),
    path('create_trip_cost/', views.create_trip_cost, name='create-trip-cost'),
    path('update_trip/update_trip_cost/<int:id>/', views.update_trip_cost, name='update-trip-cost')
]