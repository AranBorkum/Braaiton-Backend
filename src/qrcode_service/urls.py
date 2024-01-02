from django.urls import path

from qrcode_service.views import GenerateQRCodeView


GENERATE_QR_CODE_NAME = "generate-code"

urlpatterns = [
    path(
        "<uuid:payment_id>/generate-code/",
        GenerateQRCodeView.as_view(),
        name=GENERATE_QR_CODE_NAME,
    )
]
