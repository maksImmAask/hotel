from django.urls import path

from .views import (
    home,
    room_detail,
    register_view,
    login_view,
    logout_view,
    profile,
    cancel_booking
)

urlpatterns = [

    path('', home, name='home'),

    path('room/<int:pk>/', room_detail, name='room_detail'),

    path('register/', register_view, name='register'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('profile/', profile, name='profile'),

    path('cancel-booking/<int:pk>/', cancel_booking, name='cancel_booking'),
]