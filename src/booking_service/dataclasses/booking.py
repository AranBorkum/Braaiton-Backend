from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from booking_service.enums import BookingStage
from booking_service.models import BookingModel


@dataclass
class Booking:
    id: UUID
    item_id: UUID
    customer: dict
    duration: int
    start_time: datetime
    stage: BookingStage
    payment_id: UUID

    @classmethod
    def create(cls, model: BookingModel):
        return Booking(
            id=model.id,
            item_id=model.item_id,
            customer=model.customer,
            duration=model.duration,
            start_time=model.start_time,
            stage=BookingStage(model.stage),
            payment_id=model.payment_id,
        )

    def deserialize(self):
        return {
            "id": str(self.id),
            "item_id": str(self.item_id),
            "customer": self.customer,
            "duration": self.duration,
            "start_time": self.start_time,
            "stage": self.stage.value,
            "payment_id": str(self.payment_id),
        }

    def activate(self):
        self.mark_as_booked()
        self.start_time = datetime.now()
        return self

    def mark_as_booked(self):
        self.stage = BookingStage.BOOKED
        return self

    def marked_as_required_returning(self):
        self.stage = BookingStage.REQUIRES_RETURNING
        return self

    def mark_as_returned(self):
        self.stage = BookingStage.RETURNED
        return self

    def mark_as_complete(self):
        self.stage = BookingStage.COMPLETE
        return self

    def mark_as_cancelled(self):
        self.stage = BookingStage.CANCELLED
        return self
