from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login',views.user_login,name='login'),
    path('', views.signup,name='signup'),
    path('home/',views.requests,name='home'),
    path('users/<int:user_id>/', views.user_detail, name='user_profile'),
    path('update-status/<int:request_id>/', views.update_request_status, name='update_request_status'),
]