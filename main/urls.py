from django.urls import path

from .views import (
    admin_create_guest,
    admin_create_hotel,
    admin_delete_booking,
    admin_delete_guest,
    admin_delete_hotel,
    admin_edit_guest,
    admin_edit_hotel,
    admin_hotels,
    home,
    hotel_detail,
    room_detail,
    register_view,
    login_view,
    logout_view,
    profile,
    cancel_booking,
    admin_dashboard,
    admin_rooms,
    admin_create_room,
    admin_edit_room,
    admin_delete_room,
    admin_bookings,
    admin_confirm_booking,
    admin_cancel_booking_panel,
    admin_users,
    admin_create_user,
    admin_edit_user,
    admin_delete_user
)

urlpatterns = [
    path('', home, name='home'),
    path('room/<int:pk>/', room_detail, name='room_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('cancel-booking/<int:pk>/', cancel_booking, name='cancel_booking'),
    path('admin-panel/', admin_dashboard, name='admin_dashboard'),
    path('admin-panel/rooms/', admin_rooms, name='admin_rooms'),
    path('admin-panel/rooms/create/', admin_create_room, name='admin_create_room'),
    path('admin-panel/rooms/edit/<int:pk>/', admin_edit_room, name='admin_edit_room'),
    path('admin-panel/rooms/delete/<int:pk>/', admin_delete_room, name='admin_delete_room'),
    path('admin-panel/bookings/', admin_bookings, name='admin_bookings'),
    path('admin-panel/bookings/confirm/<int:pk>/', admin_confirm_booking, name='admin_confirm_booking'),
    path('admin-panel/bookings/cancel/<int:pk>/', admin_cancel_booking_panel, name='admin_cancel_booking_panel'),
    path('admin-panel/users/create/', admin_create_user, name='admin_create_user'),
    path('admin-panel/users/edit/<int:pk>/', admin_edit_user, name='admin_edit_user'),
    path('admin-panel/users/delete/<int:pk>/', admin_delete_user, name='admin_delete_user'),
    path('admin-panel/users/', admin_users, name='admin_users'),
    path('hotel/<int:pk>/', hotel_detail, name='hotel_detail'),
    path('admin-panel/hotels/', admin_hotels, name='admin_hotels'),
    path('admin-panel/hotels/create/', admin_create_hotel, name='admin_create_hotel'),
    path('admin-panel/hotels/edit/<int:pk>/', admin_edit_hotel, name='admin_edit_hotel'),
    path('admin-panel/hotels/delete/<int:pk>/', admin_delete_hotel, name='admin_delete_hotel'),
    path('admin-panel/guests/create/', admin_create_guest, name='admin_create_guest'),
    path(
        'admin-panel/guests/<int:pk>/edit/',
        admin_edit_guest,
        name='admin_edit_guest'
    ),

    path(
        'admin-panel/guests/<int:pk>/delete/',
        admin_delete_guest,
        name='admin_delete_guest'
    ),
    path(
        'admin-panel/bookings/delete/<int:pk>/',
        admin_delete_booking,
        name='admin_delete_booking'
    ),
]