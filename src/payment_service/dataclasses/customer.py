from dataclasses import dataclass
from uuid import UUID

from payment_service.models import PaymentCustomerModel


@dataclass
class Customer:
    id: UUID
    first_name: str
    last_name: str
    email: str
    phone_number: str

    @classmethod
    def create(cls, model: PaymentCustomerModel):
        return Customer(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            email=model.email,
            phone_number=model.phone_number,
        )

    def deserialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
        }
