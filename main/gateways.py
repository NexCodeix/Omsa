import json
from typing import Any, Dict, Optional

import requests


class AamarPayGateway:
    """Simple client for interacting with the AamarPay payment API."""
    # Default configuration values for the gateway
    store_id: str = "aamarpaytest"
    signature_key: str = "dbb74894e82415a2f7ff0ec3a97e4183"
    base_url: str = "https://sandbox.aamarpay.com/jsonpost.php"

    # Hard-coded callback URLs (update to your real endpoints as needed)
    success_url: str = "https://example.com/payment/success/"
    fail_url: str = "https://example.com/payment/fail/"
    cancel_url: str = "https://example.com/payment/cancel/"

    def create_payment(
        self,
        tran_id: str,
        amount: float,
        cus_name: str,
        cus_email: str,
        cus_add1: str,
        cus_add2: str,
        cus_city: str,
        cus_state: str,
        cus_postcode: str,
        cus_country: str,
        cus_phone: str,
        currency: str = "BDT",
        desc: str = "Merchant Registration Payment",
        extra_fields: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Builds and posts the AamarPay payment payload.

        Returns the parsed JSON response from AamarPay.
        """

        payload: Dict[str, Any] = {
            "store_id": self.store_id,
            "tran_id": tran_id,
            "success_url": self.success_url,
            "fail_url": self.fail_url,
            "cancel_url": self.cancel_url,
            "amount": str(amount),
            "currency": currency,
            "signature_key": self.signature_key,
            "desc": desc,
            "cus_name": cus_name,
            "cus_email": cus_email,
            "cus_add1": cus_add1,
            "cus_add2": cus_add2,
            "cus_city": cus_city,
            "cus_state": cus_state,
            "cus_postcode": cus_postcode,
            "cus_country": cus_country,
            "cus_phone": cus_phone,
            "type": "json",
        }

        if extra_fields:
            payload.update(extra_fields)
        
        headers = {"Content-Type": "application/json"}
        print(payload)

        response = requests.post(self.base_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            # Fallback if response is not JSON
            return {"raw": response.text}
