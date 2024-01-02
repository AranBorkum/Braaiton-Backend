import stripe
from stripe import PaymentIntent


STRIPE_METHOD_TYPES = ["card", "paypal"]
STRIPE_METHOD_OPTIONS = {
    "card": {
        "capture_method": "manual",
    }
}


class PaymentTokenService:
    def __init__(self, stripe_client=stripe):
        self._stripe = stripe_client
        self._stripe.api_key = "sk_test_51OLj5cBeIfC8vB4KwpoM32KEhnPTHpb5AGOXAi3VbxSSG6DN3zyjg6gLFcrzMlyHMyTOtPIHAin9jKN8nGKUZVGw00U3oKhTFk"

    def get(self, amount):
        return self._create_payment_intent(amount=amount)

    def _create_payment_intent(
        self,
        amount: int,
        currency="GBP",
    ):
        return self._stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=STRIPE_METHOD_TYPES,
            payment_method_options=STRIPE_METHOD_OPTIONS,
        )
