from rest_framework.fields import UUIDField, IntegerField
from rest_framework.serializers import Serializer


class CreateBookingSerializer(Serializer):
    item_id = UUIDField()
    duration = IntegerField()
