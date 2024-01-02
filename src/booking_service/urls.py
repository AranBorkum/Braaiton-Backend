from django.urls import path

from booking_service.views import (
    CreateBookingView,
    ActiveBookingsView,
    GetBookingView,
    CancelReservationView,
)

CREATE_BOOKING_NAME = "create"
GET_ACTIVE_BOOKINGS_NAME = "active-bookings"
GET_BOOKING_NAME = "retrieve"
CANCEL_RESERVATION_NAME = "cancel-reservation"

urlpatterns = [
    path(
        "create/",
        CreateBookingView.as_view(),
        name=CREATE_BOOKING_NAME,
    ),
    path(
        "active-bookings/",
        ActiveBookingsView.as_view(),
        name=GET_ACTIVE_BOOKINGS_NAME,
    ),
    path(
        "<uuid:booking_id>/retrieve/",
        GetBookingView.as_view(),
        name=GET_BOOKING_NAME,
    ),
    path(
        "<uuid:booking_id>/cancel-reservation/",
        CancelReservationView.as_view(),
        name=CANCEL_RESERVATION_NAME,
    ),
]
