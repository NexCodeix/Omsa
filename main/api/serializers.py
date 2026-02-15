from rest_framework import serializers


class CreatePaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    cus_name = serializers.CharField(max_length=255)
    cus_email = serializers.EmailField()
    cus_add1 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    cus_add2 = serializers.CharField(max_length=255, required=False, allow_blank=True)
    cus_city = serializers.CharField(max_length=100, required=False, allow_blank=True)
    cus_state = serializers.CharField(max_length=100, required=False, allow_blank=True)
    cus_postcode = serializers.CharField(max_length=20, required=False, allow_blank=True)
    cus_country = serializers.CharField(max_length=100, required=False, allow_blank=True)
    cus_phone = serializers.CharField(max_length=50)

