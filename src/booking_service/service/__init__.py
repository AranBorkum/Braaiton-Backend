from booking_service.dataclasses import Booking
from booking_service.repository import booking_repository
from booking_service.service.api import BookingServiceAPI
from project.base.service import BaseService


class BookingService(BaseService):
    repository = booking_repository

    def __init__(self):
        self.api = BookingServiceAPI(self)

    def get(self, booking_id: str):
        booking_model = self.repository.get_object(id=booking_id)
        return Booking.create(booking_model)

    def create(self, item_id: str, duration: int, payment_id: str, **kwargs):
        return self.repository.create_object(
            item_id=item_id,
            duration=duration,
            payment_id=payment_id,
            **kwargs,
        )

    def update(self, booking_id, booking_dataclass: Booking):
        booking_model = self.repository.get_object(id=booking_id)
        updatable_values = {
            key: value
            for key, value in booking_dataclass.deserialize().items()
            if key != "id"
        }
        self.repository.update_object(booking_model, **updatable_values)


booking_service = BookingService()
