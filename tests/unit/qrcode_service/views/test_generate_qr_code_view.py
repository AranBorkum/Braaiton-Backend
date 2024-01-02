import uuid
from unittest.mock import patch

import segno
from pytest import fixture
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

from qrcode_service.views import GenerateQRCodeView


PAYMENT_ID = uuid.uuid4()
API_ENDPOINT = f"qr/{PAYMENT_ID}/generate-code/"


@fixture
def view():
    return GenerateQRCodeView.as_view()


@fixture
def get_request():
    return APIRequestFactory().get(
        API_ENDPOINT,
        {},
        format="json",
    )


@fixture
def patch_make_qr():
    make_qr = patch.object(segno, "make_qr").start()
    yield make_qr
    make_qr.stop()


class TestCaseSuccessfulAPICall:
    def test_status_code_200(self, view, get_request, patch_make_qr):
        response: Response = view(get_request, PAYMENT_ID)
        assert response.status_code == 200

    def test_data_contains_image(self, view, get_request, patch_make_qr):
        response: Response = view(get_request, PAYMENT_ID)
        assert "image" in response.data
