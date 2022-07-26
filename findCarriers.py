import http.client
import json

conn = http.client.HTTPSConnection("api.aftership.com")
API_Key = "INPUT API KEY"

headers = {
        'Content-Type': "application/json",
        'aftership-api-key': API_Key
        }


def findCarriers(tracking):
    payload = "{\n  \"tracking\": {\n    \"tracking_number\": \"" + tracking + "\"\n  }\n}"

    conn.request("POST", "/v4/couriers/detect", payload, headers)

    res = conn.getresponse()
    data = res.read()
    data = data.decode("utf-8")
    data = json.loads(data)

    total = data["data"]["total"]
    print("Total nunber of carriers: " + str(total) + "\n")

    print("Carriers:")
    for i in data["data"]["couriers"]:
        tracking = i["name"]
        print("  " + tracking)