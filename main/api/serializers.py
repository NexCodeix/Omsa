from rest_framework import serializers


class CreatePaymentSerializer(serializers.Serializer):
    cus_name = serializers.CharField(max_length=255)
    cus_email = serializers.EmailField()
    cus_phone = serializers.CharField(max_length=50)

