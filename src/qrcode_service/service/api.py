from segno import QRCode

from project.base.service_api import ServiceAPI


class QRCodeServiceAPI(ServiceAPI):
    def generate_code_svg(self, payment_id):
        qr_code: QRCode = self._upper_class.generate(payment_id)
        return qr_code.svg_data_uri()
