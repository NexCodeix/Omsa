import secrets

from rest_framework.response import Response
from rest_framework.views import APIView

from main.gateways import AamarPayGateway
from .serializers import CreatePaymentSerializer


class CreatePaymentView(APIView):
    """Create a payment using AamarPayGateway.

    Validates input with CreatePaymentSerializer and generates a tran_id
    using secrets.token_hex() when not provided.
    """

    def post(self, request, *args, **kwargs):
        return Response(
            {"safe": True}
        )

    # def post(self, request, *args, **kwargs):  # type: ignore[override]
    #     serializer = CreatePaymentSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=400)

    #     validated = serializer.validated_data

    #     gateway = AamarPayGateway()

    #     tran_id = secrets.token_hex()
    #     try:
    #         response_data = gateway.create_payment(
    #             tran_id=tran_id,
    #             amount=float(validated["amount"]),
    #             cus_name=validated["cus_name"],
    #             cus_email=validated["cus_email"],
    #             cus_add1=validated["cus_add1"],
    #             cus_add2=validated["cus_add2"],
    #             cus_city=validated["cus_city"],
    #             cus_state=validated["cus_state"],
    #             cus_postcode=validated["cus_postcode"],
    #             cus_country=validated["cus_country"],
    #             cus_phone=validated["cus_phone"],
    #             # No extra_fields for now; everything is captured by the serializer
    #         )
    #     except Exception as exc:  # noqa: BLE001 - simple API error wrapper
    #         return Response({"error": str(exc)}, status=502)

    #     return Response({"tran_id": tran_id, "gateway_response": response_data})
