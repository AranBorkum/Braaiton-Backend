from rest_framework import status

from booking_service.dataclasses import Booking
from booking_service.enums import BookingStage
from booking_service.models import BookingModel
from inventory_service.dataclasses.inventory_item import InventoryItem
from inventory_service.service import inventory_service
from payment_service.service import payment_service
from project.base.service_api import ServiceAPI


BOOKING_ACTIVE_STATES = {
    BookingStage.RESERVED.value,
    BookingStage.BOOKED.value,
    BookingStage.REQUIRES_RETURNING.value,
}


class BookingServiceAPI(ServiceAPI):
    def create_booking(
        self,
        item_id: str,
        duration: int,
    ):
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {"message": "something went wrong"}

        payment_model = payment_service.create()
        booking_model: BookingModel = self._upper_class.create(
            item_id,
            duration,
            str(payment_model.id),
        )

        if booking_model:
            response_status = status.HTTP_200_OK
            response_data = Booking.create(booking_model).deserialize()

        payment_service.update_params(payment_model, booking=booking_model)
        inventory_service.reserve_item_by_id(item_id)

        return response_status, response_data

    def activate_booking(self, booking_id: str):
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {"message": "something went wrong"}

        booking: Booking = self._upper_class.get(booking_id)
        booking: Booking = booking.activate()
        self._upper_class.update(booking_id, booking)

        if booking:
            response_status = status.HTTP_200_OK
            response_data = booking.deserialize()

        return response_status, response_data

    def get_active_bookings(self):
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {"message": "something went wrong"}

        booking_models = self._upper_class.repository.get_objects(
            stage__in=BOOKING_ACTIVE_STATES
        )

        if booking_models:
            response_status = status.HTTP_200_OK
            response_data = [
                Booking.create(model).deserialize() for model in booking_models
            ]

        return response_status, response_data

    def get_booking(self, booking_id: str):
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {"message": "something went wrong"}

        booking: Booking = self._upper_class.get(booking_id)

        if booking:
            response_status = status.HTTP_200_OK
            response_data = booking.deserialize()

        return response_status, response_data

    def cancel_reservation(self, booking_id: str):
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {"message": "something went wrong"}

        booking: Booking = self._upper_class.get(booking_id)

        if booking:
            booking.mark_as_cancelled()
            self._upper_class.update(booking_id, booking)
            inventory_service.deallocate_item_by_id(booking.item_id)

            response_status = status.HTTP_200_OK
            response_data = booking.deserialize()

        return response_status, response_data
