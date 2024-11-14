from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.requests,name='home'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('update-status/<int:request_id>/', views.update_request_status, name='update_request_status'),
]