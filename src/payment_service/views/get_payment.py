from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from payment_service.service import payment_service


class GetPaymentView(APIView):
    def get(self, request: Request, payment_id: str):
        request_status, request_data = payment_service.api.get_payment(
            payment_id=payment_id
        )
        return Response(request_data, status=request_status)
