from inventory_service.models import InventoryModel
from project.base.repository import BaseRepository


class InventoryRepository(BaseRepository):
    object_model = InventoryModel


inventory_repository = InventoryRepository()
