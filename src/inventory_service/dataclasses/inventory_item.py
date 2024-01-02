from dataclasses import dataclass
from uuid import UUID

from inventory_service.enums import InventoryState
from inventory_service.models import InventoryModel


@dataclass
class InventoryItem:
    id: UUID
    name: str
    description: str
    cost_per_hour: int
    state: InventoryState

    @classmethod
    def create(cls, model: InventoryModel):
        return InventoryItem(
            id=model.id,
            name=model.name,
            description=model.description,
            cost_per_hour=model.cost_per_hour,
            state=InventoryState(model.state),
        )

    def deserialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "cost_per_hour": self.cost_per_hour,
            "state": self.state.value,
        }

    def mark_as_reserved(self):
        self.state = InventoryState.RESERVED
        return self

    def mark_as_available(self):
        self.state = InventoryState.AVAILABLE
        return self
