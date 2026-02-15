import requests
import json

url = "https://sandbox.aamarpay.com/jsonpost.php"

payload = json.dumps({
  "store_id": "aamarpaytest",
  "tran_id": "1231231731231231231asdsad23123sadsad",
  "success_url": "http://www.merchantdomain.com/successpage.html",
  "fail_url": "http://www.merchantdomain.com/failedpage.html",
  "cancel_url": "http://www.merchantdomain.com/cancelpage.html",
  "amount": "10.0",
  "currency": "BDT",
  "signature_key": "dbb74894e82415a2f7ff0ec3a97e4183",
  "desc": "Merchant Registration Payment",
  "cus_name": "Name",
  "cus_email": "payer@merchantcusomter.com",
  "cus_add1": "House B-158 Road 22",
  "cus_add2": "Mohakhali DOHS",
  "cus_city": "Dhaka",
  "cus_state": "Dhaka",
  "cus_postcode": "1206",
  "cus_country": "Bangladesh",
  "cus_phone": "+8801704",
  "type": "json"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
