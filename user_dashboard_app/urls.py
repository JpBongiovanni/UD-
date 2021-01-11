from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('sign_in', views.sign_in_page),
    path('register', views.register_page),
    path('user_info', views.user_info_page),
    path('user_dashboard', views.user_dashboard_page),
    path('edit_user', views.edit_profile_page),
    path('admin_dashboard', views.admin_dashboard_page),
    
]