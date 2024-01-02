from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from inventory_service.serializers import InventoryModelSerializer
from inventory_service.service import inventory_service


class AddInventoryModelView(APIView):
    def post(self, request: Request):
        serializer = InventoryModelSerializer(data=request.data)
        response_status = status.HTTP_400_BAD_REQUEST
        data = {"message": "something went wrong"}

        if serializer.is_valid():
            response_status, data = inventory_service.api.add_inventory_item(
                serializer.validated_data
            )

        return Response(data, status=response_status)
