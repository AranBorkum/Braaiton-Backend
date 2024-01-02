import uuid

from django.db.models import (
    CharField,
    IntegerField,
    Model,
    TextField,
    UUIDField,
)

from inventory_service.enums import InventoryState


class InventoryModel(Model):
    id = UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = CharField(max_length=100)
    description = TextField()
    cost_per_hour = IntegerField()
    state = IntegerField(default=InventoryState.AVAILABLE.value)
