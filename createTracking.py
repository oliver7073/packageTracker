import http.client
import json

def createTracking(title, courier, trackingNumber):

    conn = http.client.HTTPSConnection("api.aftership.com")

    headers = {
            'Content-Type': "application/json",
            'aftership-api-key': "fe794360-ef83-4ca1-82db-77b6259b4757"
            }

    payload = "{\n  \"tracking\": {\n    \"slug\": \"" + courier + "\",\n    \"tracking_number\": \""+ trackingNumber +"\",\n    \"title\": \""+ title +"\",\n    \"smses\": [\n      \"\",\n      \"\"\n    ],\n    \"emails\": [\n      \"\",\n      \"\"\n    ],\n    \"order_id\": \"\",\n    \"order_number\": \"\",\n    \"order_id_path\": \"\",\n    \"custom_fields\": {\n      \"product_name\": \"\",\n      \"product_price\": \"\"\n    },\n    \"language\": \"\",\n    \"order_promised_delivery_date\": \"\",\n    \"delivery_type\": \"\",\n    \"pickup_location\": \"\",\n    \"pickup_note\": \"\"\n  }\n}"

    conn.request("POST", "/v4/trackings", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
    print("Your package has been added to the system!")