from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from qrcode_service.service import qr_service


class GenerateQRCodeView(APIView):
    def get(self, request: Request, payment_id: str):
        qr_code_svg = qr_service.api.generate_code_svg(payment_id)
        return Response({"image": qr_code_svg})
