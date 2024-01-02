import uuid
from unittest.mock import patch

import segno
from django.test import override_settings
from pytest import fixture

from qrcode_service.service import qr_service

PAYMENT_ID = uuid.uuid4()


@fixture
def service():
    return qr_service


@fixture
def patch_make_qr():
    make_qr = patch.object(segno, "make_qr").start()
    yield make_qr
    make_qr.stop()


class TestCaseQRService:
    @override_settings(
        QR_CODE_PROTOCOL="protocol",
        QR_CODE_DOMAIN="domain",
        QR_CODE_PORT="port",
    )
    def test_generate_called_with_expected_values(self, service, patch_make_qr):
        service.generate(payment_id=PAYMENT_ID)
        patch_make_qr.assert_called_with(f"protocol://domain:port/payment/{PAYMENT_ID}")
