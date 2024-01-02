from django.urls import path

from inventory_service.views import (
    AddInventoryModelView,
    GetAvailableModelsView,
    GetInventoryItemView,
    MarkInventoryItemAsUnavailableView,
    MarkInventoryItemAsAvailableView,
)

ADD_INVENTORY_ITEM_NAME = "add-item"
GET_AVAILABLE_MODELS_NAME = "get-available-models"
GET_INVENTORY_ITEM_NAME = "retrieve"
MARK_AS_AVAILABLE_NAME = "mark-as-available"
MARK_AS_UNAVAILABLE_NAME = "mark-as-unavailable"


urlpatterns = [
    path(
        "add-item/",
        AddInventoryModelView.as_view(),
        name=ADD_INVENTORY_ITEM_NAME,
    ),
    path(
        "get-available-models/",
        GetAvailableModelsView.as_view(),
        name=GET_AVAILABLE_MODELS_NAME,
    ),
    path(
        "<uuid:item_id>/retrieve/",
        GetInventoryItemView.as_view(),
        name=GET_INVENTORY_ITEM_NAME,
    ),
    path(
        "<uuid:item_id>/mark-as-available/",
        MarkInventoryItemAsAvailableView.as_view(),
        name=MARK_AS_AVAILABLE_NAME,
    ),
    path(
        "<uuid:item_id>/mark-as-unavailable/",
        MarkInventoryItemAsUnavailableView.as_view(),
        name=MARK_AS_UNAVAILABLE_NAME,
    ),
]
