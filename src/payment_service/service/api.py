from rest_framework import status
from stripe import PaymentIntent

from payment_service.dataclasses import Customer
from project.base.service_api import ServiceAPI


class PaymentServiceAPI(ServiceAPI):
    def get_payment_token(self):
        request_status = status.HTTP_400_BAD_REQUEST
        request_data = {"message": "something went wrong"}

        payment_intent: PaymentIntent = self._upper_class.token.get(1000)

        if client_secret := payment_intent.client_secret:
            request_status = status.HTTP_200_OK
            request_data = {
                "client_secret": client_secret,
                "payment_intent_id": payment_intent.id,
            }

            self._upper_class.repository.create_object(
                amount=payment_intent.amount,
                payment_intent_id=payment_intent.id,
            )

        return request_status, request_data

    def create_payment_customer(self, payment_id: str, **kwargs):
        request_status = status.HTTP_400_BAD_REQUEST
        request_data = {"message": "something went wrong"}

        if payment_customer_model := self._upper_class.repository.create_payment_customer(
            **kwargs
        ):
            payment_model = self._upper_class.repository.get_object(id=payment_id)
            self._upper_class.update_params(
                payment_model, customer=payment_customer_model
            )
            payment_customer: Customer = Customer.create(payment_customer_model)
            request_status = status.HTTP_200_OK
            request_data = payment_customer.deserialize()

        return request_status, request_data

    def get_payment(self, payment_id: str):
        request_status = status.HTTP_400_BAD_REQUEST
        request_data = {"message": "something went wrong"}

        if payment := self._upper_class.get(payment_id):
            request_status = status.HTTP_200_OK
            request_data = payment.deserialize()

        return request_status, request_data
