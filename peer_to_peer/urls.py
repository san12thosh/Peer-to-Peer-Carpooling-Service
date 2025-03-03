from django.urls import path
from . import views
from .views import get_balance,calculate_fare,payment,payment_success,rider_balance

urlpatterns= [
    path('home/', views.home, name='home'),
    path('login_rider/',views.login_rider,name='login_rider'),
    path('login_user/',views.login_user,name='login_user'),
    path('create-account/', views.create_account, name='create_account'),
    path('two_verify/', views.two_verify, name='two_verify'),
    path('create_rider_acc/', views.create_rider_acc, name='create_rider_acc'),
    path('rider_path/', views.rider_path, name='rider_path'),
    path('user_path/', views.user_path, name='user_path'),
    path('map_leaflet/', views.map_leaflet, name='map_leaflet'),
    path('map_user/', views.map_user, name='map_user'),
    path('preference/', views.preference, name='preference'),
    path('matching_passengers/', views.matching_passengers, name='matching_passengers'),
    path('display_rider/', views.display_rider, name='display_rider'),
    path('get_balance/', views.get_balance, name='get_balance'),
    path('calculate_fare/', calculate_fare, name='calculate_fare'),
    path('payment/', payment, name='payment'),
    path('payment_success/', payment_success, name='payment_success'),
    path('rider_balance/', views.rider_balance, name='rider_balance'),
]