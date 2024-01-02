from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from payment_service.serializers import CreatePaymentCustomerSerializer
from payment_service.service import payment_service


class CreatePaymentCustomerView(APIView):
    def post(self, request: Request, payment_id: str):
        request_status = status.HTTP_400_BAD_REQUEST
        request_data = {"message": "something went wrong"}

        serializer = CreatePaymentCustomerSerializer(data=request.data)
        if serializer.is_valid():
            request_status, request_data = payment_service.api.create_payment_customer(
                payment_id=payment_id, **serializer.validated_data
            )

        return Response(request_data, status=request_status)
