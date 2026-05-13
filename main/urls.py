from django.urls import path

from .views import (
    home,
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

    path( 'admin-panel/rooms/edit/<int:pk>/', admin_edit_room, name='admin_edit_room'),

    path( 'admin-panel/rooms/delete/<int:pk>/', admin_delete_room, name='admin_delete_room'),

    path( 'admin-panel/bookings/', admin_bookings, name='admin_bookings'),

    path( 'admin-panel/bookings/confirm/<int:pk>/', admin_confirm_booking, name='admin_confirm_booking'),
    path( 'admin-panel/bookings/cancel/<int:pk>/', admin_cancel_booking_panel, name='admin_cancel_booking_panel'
    ),
    path( 'admin-panel/users/create/', admin_create_user, name='admin_create_user'),

    path( 'admin-panel/users/edit/<int:pk>/', admin_edit_user, name='admin_edit_user'),

    path( 'admin-panel/users/delete/<int:pk>/', admin_delete_user, name='admin_delete_user'
    ),
    path( 'admin-panel/users/', admin_users, name='admin_users'),
]