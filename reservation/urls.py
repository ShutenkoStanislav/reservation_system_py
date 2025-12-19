from django.urls import path, include
from reservation import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rooms_list/", views.room_list, name="room_list"),
    path("room/<int:room_id>/", views.room_details, name="room_details"),
    path("book_room/<int:room_id>/book/", views.book_room, name="book_room"),
    path("booking_details/<int:pk>/", views.booking_details, name="booking_details"),
    path('accounts/', include('auth_system.urls')),
    path("profile/", views.profile_details, name="profile_detail"),
]


