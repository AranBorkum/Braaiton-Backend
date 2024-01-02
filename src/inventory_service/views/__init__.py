from inventory_service.views.add_inventory_model import AddInventoryModelView
from inventory_service.views.get_available_models import GetAvailableModelsView
from inventory_service.views.get_item_availablity import GetInventoryItemView
from inventory_service.views.mark_as_available import MarkInventoryItemAsAvailableView
from inventory_service.views.mark_as_unavailable import (
    MarkInventoryItemAsUnavailableView,
)

__all__ = [
    "AddInventoryModelView",
    "GetAvailableModelsView",
    "GetInventoryItemView",
    "MarkInventoryItemAsAvailableView",
    "MarkInventoryItemAsUnavailableView",
]
