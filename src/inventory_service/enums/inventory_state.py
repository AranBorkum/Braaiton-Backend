from enum import Enum, auto


class InventoryState(Enum):
    AVAILABLE = auto()
    RESERVED = auto()
    IN_USE = auto()
