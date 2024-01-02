import uuid

from django.db.models import (
    Model,
    UUIDField,
    IntegerField,
    CharField,
    ForeignKey,
    CASCADE,
    EmailField,
)

from booking_service.models import BookingModel


class PaymentModel(Model):
    id = UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    amount = IntegerField()
    payment_intent_id = CharField(max_length=100, unique=True, null=True)
    client_secret = CharField(max_length=200, unique=True, null=True)
    customer = ForeignKey("PaymentCustomerModel", on_delete=CASCADE, null=True)
    booking = ForeignKey(BookingModel, on_delete=CASCADE, null=True)


class PaymentCustomerModel(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    email = EmailField()
    phone_number = CharField(max_length=20)
