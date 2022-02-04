import requests
import sys

#api22 ='01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'
prod_api = '017d1f0298ca0b9c02_89F736A27B08E31A6919E8DC72F54DC69F5B53C6D0B0E7690564A50D6A4D976A'
seaturl = 'https://pki-ws-rest.symauth.com/mpki/api/v1/seat'
# Email retrived from SMAX
email = sys.argv[1]
common_name = sys.argv[2]
# Common Name retrived from SMAX
seat_id = common_name
# Common Name retrived from SMAX
seat_name = common_name
#seatid = 'mc4w01851.itcs.softwaregrp.net'
#seat_nameid = 'mc4w01851.itcs.softwaregrp.net'

payload = f"""{{
  "email" : "{email}",
  "seat_id" : "{seat_id}",
  "seat_name" : "{seat_name}"
}}
"""
headers = {
    'X-API-Key': prod_api,
    'Content-Type': "application/json"
    }

resp = requests.post(seaturl, data=payload, headers=headers)
print(resp.text)
print(resp.status_code)