from inventory_service.dataclasses.inventory_item import InventoryItem
from inventory_service.repository import inventory_repository
from inventory_service.service.api import InventoryServiceAPI
from project.base.service import BaseService


class InventoryService(BaseService):
    repository = inventory_repository

    def __init__(self):
        self.api = InventoryServiceAPI(self)

    def get(self, item_id: str):
        inventory_model = self.repository.get_object(id=item_id)
        return InventoryItem.create(inventory_model)

    def update(self, item_id: str, item: InventoryItem):
        inventory_model = self.repository.get_object(id=item_id)
        updatable_values = {
            key: value for key, value in item.deserialize().items() if key != "id"
        }
        self.repository.update_object(inventory_model, **updatable_values)

    def reserve_item_by_id(self, item_id: str) -> None:
        item: InventoryItem = self.get(item_id)
        item: InventoryItem = item.mark_as_reserved()
        self.update(item_id, item)

    def deallocate_item_by_id(self, item_id: str) -> None:
        item: InventoryItem = self.get(item_id)
        item: InventoryItem = item.mark_as_available()
        self.update(item_id, item)


inventory_service = InventoryService()
