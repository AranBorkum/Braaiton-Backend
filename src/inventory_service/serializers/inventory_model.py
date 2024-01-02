from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer


class InventoryModelSerializer(Serializer):
    name = CharField()
    description = CharField()
    cost_per_hour = IntegerField()
