from rest_framework.serializers import Serializer, CharField, EmailField


class CreatePaymentCustomerSerializer(Serializer):
    first_name = CharField()
    last_name = CharField()
    email = EmailField()
    phone_number = CharField()
