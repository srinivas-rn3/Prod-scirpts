import requests

import json
import sys


api22 ='01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'

url = "https://pki-ws-rest.symauth.com/mpki/api/v1/seat/"

#seatid = 'm9w0054g.houston.softwaregrp.net'

common_name = sys.argv[1]

seatid = common_name

email = sys.argv[2]

certurl = url+seatid

payload ={

  "email" : email,

  "seat_name" : seatid

}

headers = {

    'X-API-Key': api22,

    'Content-Type': "application/json"

    }

payload_new = json.dumps(payload)

resp = requests.put(certurl, data=payload_new, headers=headers)

#print(resp.text)

print(resp.status_code)