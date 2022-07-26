import http.client
import json

conn = http.client.HTTPSConnection("api.aftership.com")
API_Key = "INPUT API KEY"

headers = {
        'Content-Type': "application/json",
        'aftership-api-key': API_Key
        }

def packageStatus(courier, trackingNumber):
    conn.request("GET", "/v4/trackings/" + courier + "/" + trackingNumber, headers=headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)
#     print(data)

#     created_at = data["data"]["tracking"]["created_at"]
#     updated_at = data["data"]["tracking"]["updated_at"]
#     last_updated_at = data["data"]["tracking"]["last_updated_at"]
    tracking_number = data["data"]["tracking"]["tracking_number"]
    slug = data["data"]["tracking"]["slug"]
    delivery_time = data["data"]["tracking"]["delivery_time"]
    shipment_pickup_date = data["data"]["tracking"]["shipment_pickup_date"]
    shipment_delivery_date = data["data"]["tracking"]["shipment_delivery_date"]
    shipment_type = data["data"]["tracking"]["shipment_type"]
    shipment_weight = data["data"]["tracking"]["shipment_weight"]
    shipment_weight_unit = data["data"]["tracking"]["shipment_weight_unit"]
    expectedDelivery = data["data"]["tracking"]["expected_delivery"]


    print("Courier: " + str(slug))
    print("Tracking number: " + str(tracking_number) + "\n")
    

    print("Pickup Date: " + str(shipment_pickup_date))
    print("Expected Delivery: " + str(expectedDelivery) + "\n")

    print("Delivery Date: " + str(shipment_delivery_date))
    print("Delivery Time: " + str(delivery_time) + " days")
    