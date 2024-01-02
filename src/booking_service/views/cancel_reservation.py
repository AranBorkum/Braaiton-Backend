from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from booking_service.service import booking_service


class CancelReservationView(APIView):
    def post(self, request: Request, booking_id: str):
        request_status, request_data = booking_service.api.cancel_reservation(
            booking_id
        )
        return Response(request_data, status=request_status)
