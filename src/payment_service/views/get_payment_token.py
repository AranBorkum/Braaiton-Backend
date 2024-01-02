from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from payment_service.service import payment_service


class GetPaymentToken(APIView):
    def post(self, request: Request):
        request_status, request_data = payment_service.api.get_payment_token()
        return Response(request_data, status=request_status)
