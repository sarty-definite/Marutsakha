from pymavlink import mavutil
import requests
import json
import datetime

url = "https://ap-south-1.aws.data.mongodb-api.com/app/data-eauco/endpoint/data/v1/action/insertOne"

headers = {
  'Content-Type': 'application/ejson',
  'Access-Control-Request-Headers': '*',
  'api-key':"ENTER API KEY HERE",
}

master = mavutil.mavlink_connection('udp:localhost:14445')
while True:
    msg = master.recv_msg()
    if msg is not None and msg.get_type()=="GPS_RAW_INT":
        print(msg.lat)
        print(msg.lon)
        
        payload = json.dumps({
            "collection": "Trashtrack",
            "database": "Trashtrack",
            "dataSource": "Cluster0",
            "document": {
        "lat":msg.lat,
        "long":msg.lon,
        "time":datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
            }
        })

        response = requests.request("POST", url, headers=headers, data=payload)

        # print(response.text)