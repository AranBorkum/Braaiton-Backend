from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from booking_service.serializers import CreateBookingSerializer
from booking_service.service import booking_service


class CreateBookingView(APIView):
    def post(self, request: Request):
        serializer = CreateBookingSerializer(data=request.data)
        response_status = status.HTTP_400_BAD_REQUEST
        data = {"message": "something went wrong"}

        if serializer.is_valid():
            response_status, data = booking_service.api.create_booking(
                **serializer.validated_data
            )

        return Response(data, status=response_status)
