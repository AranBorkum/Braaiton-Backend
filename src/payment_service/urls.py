from django.urls import path

from payment_service.views import (
    GetPaymentToken,
    CreatePaymentCustomerView,
    GetPaymentView,
)

GET_PAYMENT_TOKEN_NAME = "get-token"
CREATE_CUSTOMER_NAME = "create-customer"
GET_PAYMENT_NAME = "get-payment"

urlpatterns = [
    path(
        "get-token/",
        GetPaymentToken.as_view(),
        name=GET_PAYMENT_TOKEN_NAME,
    ),
    path(
        "<uuid:payment_id>/create-customer/",
        CreatePaymentCustomerView.as_view(),
        name=CREATE_CUSTOMER_NAME,
    ),
    path(
        "<uuid:payment_id>/get-payment/",
        GetPaymentView.as_view(),
        name=GET_PAYMENT_NAME,
    ),
]
