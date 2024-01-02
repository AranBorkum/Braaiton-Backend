from rest_framework.views import APIView


class BaseAPIView(APIView):
    response_status: int
    response_data: dict
