from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory_service.service import inventory_service


class GetInventoryItemView(APIView):
    def get(self, request: Request, item_id: str):
        response_status, response_data = inventory_service.api.get_inventory_item(
            item_id=item_id
        )
        return Response(response_data, status=response_status)
