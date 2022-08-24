import requests
import json

url = "https://secure.clickpay.com.sa/payment/new/invoice"

payload = "{\n    \"profile_id\": 59313 ,\n    \"tran_type\": \"sale\",\n    \"tran_class\": \"ecom\",\n    \"cart_currency\": \"AED\",\n    \"cart_amount\": \"9.5\",\n    \"cart_id\": \"cart_12345\",\n    \"cart_description\": \"Test Description\",\n    \"hide_shipping\": true,\n    \"customer_ref\":\"CUST0101\",\n    \"customer_details\": {\n        \"name\": \"First Last\",\n        \"email\": \"wj@email.com\",\n        \"street1\": \"404, 11th st, void\",\n        \"city\": \"Dubai\",\n        \"country\": \"AE\"\n    },\n    \"invoice\": {\n        \"shipping_charges\": 0,\n        \"extra_charges\": 0,\n        \"extra_discount\": 0,\n        \"total\": 0,\n        \"activation_date\": \"\",\n        \"expiry_date\": \"2022-09-27T13:33:00+04:00\",\n        \"due_date\": \"2022-09-26T12:36:00+04:00\",\n        \"line_items\": [\n            {\n                \"sku\": \"sku\",\n                \"description\": \"desc\",\n                \"url\": \"https://www.costacoffee.ae/whats-new/flat-white\",\n                \"unit_cost\": 9.5,\n                \"quantity\": 1,\n                \"net_total\": 9.5,\n                \"discount_rate\": 0,\n                \"discount_amount\": 0,\n                \"tax_rate\": 0,\n                \"tax_total\": 0,\n                \"total\": 9.5\n            }\n        ]\n    },\n    \"callback\": \"\",\n    \"return\": \"\"\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)