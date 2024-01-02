from payment_service.models import PaymentModel, PaymentCustomerModel
from project.base.repository import BaseRepository


class PaymentRepository(BaseRepository):
    object_model = PaymentModel

    @staticmethod
    def create_payment_customer(**kwargs):
        return PaymentCustomerModel.objects.create(**kwargs)


payment_repository = PaymentRepository()
