from payment_service.dataclasses import Payment
from payment_service.repository import payment_repository
from payment_service.service.api import PaymentServiceAPI
from payment_service.service.token import PaymentTokenService


from project.base.service import BaseService


class PaymentService(BaseService):
    repository = payment_repository

    def __init__(self):
        self.token = PaymentTokenService()
        self.api = PaymentServiceAPI(self)

    def get(self, payment_id: str) -> Payment:
        payment_model = self.repository.get_objects(id=payment_id).last()
        if payment_model:
            return Payment.create(payment_model)

    def create(self, **kwargs):
        payment_intent = self.token.get(amount=1000)
        return self.repository.create_object(
            amount=1000,
            payment_intent_id=payment_intent.id,
            client_secret=payment_intent.client_secret,
        )

    def update(self, payment_id: str, payment: Payment):
        payment_model = self.repository.get_object(id=payment_id)
        update_values = {
            key: value for key, value in payment.deserialize().items() if key != "id"
        }
        self.repository.update_object(payment_model, update_values)

    def update_params(self, obj, **parameters):
        self.repository.update_object(obj, **parameters)


payment_service = PaymentService()
