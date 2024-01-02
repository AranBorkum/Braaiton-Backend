from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from booking_service.service import booking_service


class ActivateBookingView(APIView):
    def post(self, request: Request, booking_id: str):
        response_status, response_data = booking_service.api.activate_booking(
            booking_id
        )
        return Response(response_data, status=response_status)
