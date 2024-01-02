from dataclasses import dataclass
from uuid import UUID

from booking_service.dataclasses import Booking
from payment_service.dataclasses.customer import Customer
from payment_service.models import PaymentModel


@dataclass
class Payment:
    id: UUID
    amount: int
    payment_intent_id: str
    client_secret: str
    customer: Customer
    booking: Booking

    @classmethod
    def create(cls, model: PaymentModel):
        customer = Customer.create(model.customer) if model.customer else model.customer
        booking = Booking.create(model.booking) if model.booking else model.booking

        return Payment(
            id=model.id,
            amount=model.amount,
            payment_intent_id=model.payment_intent_id,
            client_secret=model.client_secret,
            customer=customer,
            booking=booking,
        )

    def deserialize(self):
        customer = self.customer.deserialize() if self.customer else self.customer
        booking = self.booking.deserialize() if self.booking else self.booking

        return {
            "id": self.id,
            "amount": self.amount,
            "payment_intent_id": self.payment_intent_id,
            "client_secret": self.client_secret,
            "customer": customer,
            "booking": booking,
        }
