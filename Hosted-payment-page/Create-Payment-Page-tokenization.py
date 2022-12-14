import requests
import json

url = "https://secure.clickpay.com.sa/payment/request"

payload = "{\n    \"profile_id\": 59313  ,\n    \"tran_type\": \"sale\",\n    \"tran_class\": \"ecom\",\n    \"tokenise\": \"2\",\n    \"cart_id\": \"cart_444441\",\n    \"cart_currency\": \"AED\",\n    \"cart_amount\": 1,\n    \"cart_description\": \"Payment with tok enabled, save card enabled\",\n    \"show_save_card\": false,\n    \"customer_details\": {\n        \"name\": \"first last\",\n        \"email\": \"email@domain.com\",\n        \"phone\": \"0522222222\",\n        \"street1\": \"address street\",\n        \"city\": \"dubai\",\n        \"state\": \"du\",\n        \"country\": \"AE\",\n        \"zip\": \"12345\"\n    },\n    \"shipping_details\": {\n        \"name\": \"name1 last1\",\n        \"email\": \"email1@domain.com\",\n        \"phone\": \"971555555555\",\n        \"street1\": \"street2\",\n        \"city\": \"dubai\",\n        \"state\": \"dubai\",\n        \"country\": \"AE\",\n        \"zip\": \"54321\"\n    },\n    \"callback\": \"\",\n    \"return\": \"\",\n    \"hide_shipping\": true\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

json_object = json.loads(response.text)

print("ClickPay Url is " + json_object["redirect_url"])

