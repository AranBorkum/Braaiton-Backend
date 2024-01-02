from rest_framework import status

from inventory_service.dataclasses.inventory_item import InventoryItem
from inventory_service.enums import InventoryState
from inventory_service.models import InventoryModel
from project.base.service_api import ServiceAPI


class InventoryServiceAPI(ServiceAPI):
    def add_inventory_item(self, validated_inventory_values: dict):
        response_status: int = status.HTTP_400_BAD_REQUEST
        response_data: dict = {"message": "something went wrong"}

        inventory_model: InventoryModel = self._upper_class.repository.create_object(
            **validated_inventory_values
        )
        if inventory_model:
            response_status = status.HTTP_201_CREATED
            response_data = {
                "message": f"Successfully created inventory model {inventory_model.name}"
            }

        return response_status, response_data

    def get_available_items(self):
        available_items = [
            InventoryItem.create(model)
            for model in self._upper_class.repository.get_objects(
                state=InventoryState.AVAILABLE.value
            )
        ]
        response_status: int = status.HTTP_200_OK
        response_data: list = [item.deserialize() for item in available_items]
        return response_status, response_data

    def get_inventory_item(self, item_id: str):
        response_status: int = status.HTTP_400_BAD_REQUEST
        response_data: dict = {"message": "something went wrong"}

        inventory_item: InventoryItem = self._upper_class.get(item_id)
        if inventory_item:
            response_status = status.HTTP_200_OK
            response_data = inventory_item.deserialize()

        return response_status, response_data

    def mark_as_unavailable(self, item_id: str):
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {"message": "something went wrong"}

        inventory_item: InventoryItem = self._upper_class.get(item_id)
        if inventory_item:
            try:
                inventory_item.mark_as_unavailable()
                self._upper_class.update(inventory_item.id, inventory_item)
                response_status = status.HTTP_200_OK
                response_data = {str(inventory_item.id): inventory_item.deserialize()}
            except AttributeError:
                response_status = status.HTTP_226_IM_USED
                response_data = {
                    "message": f"Item {inventory_item.id} is already unavailable",
                    str(inventory_item.id): inventory_item.deserialize(),
                }

        return response_status, response_data

    def mark_as_available(self, item_id: str):
        response_status = status.HTTP_400_BAD_REQUEST
        response_data = {"message": "something went wrong"}

        inventory_item: InventoryItem = self._upper_class.get(item_id)
        if inventory_item:
            try:
                inventory_item.mark_as_available()
                self._upper_class.update(inventory_item.id, inventory_item)
                response_status = status.HTTP_200_OK
                response_data = {str(inventory_item.id): inventory_item.deserialize()}
            except AttributeError:
                response_status = status.HTTP_226_IM_USED
                response_data = {
                    "message": f"Item {inventory_item.id} is already available",
                    str(inventory_item.id): inventory_item.deserialize(),
                }

        return response_status, response_data
