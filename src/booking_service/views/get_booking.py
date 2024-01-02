from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from booking_service.service import booking_service


class GetBookingView(APIView):
    def get(self, request: Request, booking_id: str):
        request_status, request_data = booking_service.api.get_booking(booking_id)
        return Response(request_data, status=request_status)
