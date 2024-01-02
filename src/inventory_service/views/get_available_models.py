from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory_service.service import inventory_service


class GetAvailableModelsView(APIView):
    def get(self, request: Request):
        response_status, response_data = inventory_service.api.get_available_items()
        return Response(response_data, status=response_status)
