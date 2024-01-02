import uuid

from django.db.models import (
    Model,
    UUIDField,
    JSONField,
    IntegerField,
    DateTimeField,
)

from booking_service.enums import BookingStage


class BookingModel(Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    item_id = UUIDField()
    customer = JSONField(null=True)
    duration = IntegerField(default=2)
    start_time = DateTimeField(null=True)
    stage = IntegerField(default=BookingStage.RESERVED.value)
    payment_id = UUIDField(null=True)
