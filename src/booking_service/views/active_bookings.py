from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from booking_service.service import booking_service


class ActiveBookingsView(APIView):
    def get(self, request: Request):
        response_status, response_data = booking_service.api.get_active_bookings()
        return Response(response_data, status=response_status)
