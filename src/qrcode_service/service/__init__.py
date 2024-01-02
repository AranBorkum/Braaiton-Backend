import segno
from django.conf import settings

from qrcode_service.service.api import QRCodeServiceAPI


class QRService:
    def __init__(self):
        self.api = QRCodeServiceAPI(self)

    def generate(self, payment_id):
        payment_link_url = (
            f"{settings.QR_CODE_PROTOCOL}://"
            f"{settings.QR_CODE_DOMAIN}:"
            f"{settings.QR_CODE_PORT}"
            f"/payment/{payment_id}"
        )
        return segno.make_qr(payment_link_url)


qr_service = QRService()
