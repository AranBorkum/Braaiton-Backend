from enum import Enum, auto


class BookingStage(Enum):
    RESERVED = auto()
    BOOKED = auto()
    REQUIRES_RETURNING = auto()
    RETURNED = auto()
    COMPLETE = auto()
    CANCELLED = auto()
