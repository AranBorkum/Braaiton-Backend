from booking_service.models import BookingModel
from project.base.repository import BaseRepository


class BookingRepository(BaseRepository):
    object_model = BookingModel


booking_repository = BookingRepository()
