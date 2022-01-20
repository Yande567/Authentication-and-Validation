from django.urls import path
from . import views

urlpatterns = [
    path('country_selection', views.country_selection, name='country_selection'),
    path('get_json_response/', views.get_json_country_data, name='get_json_response'),
    path('province_json/<str:country>/', views.get_json_province_data, name='province_json'),
    path('city_json/<str:province>/', views.get_json_city_data, name='city_json'),
    path('save_country_selection/', views.save_country_info, name='save_country_selection'),
]
