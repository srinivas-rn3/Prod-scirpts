import requests
import sys

#api22 ='01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'
prod_api = '017d1f0298ca0b9c02_89F736A27B08E31A6919E8DC72F54DC69F5B53C6D0B0E7690564A50D6A4D976A'

url = "https://pki-ws-rest.symauth.com/mpki/api/v1/seat/"

#seatid = 'm9w0054g.houston.softwaregrp.net'

#SeatID retrived from SMAX
#common_name = "m9w0144g.houston.softwaregrp.net"
common_name = sys.argv[1]
seatid = common_name
#seatid = 'mc4w01851.itcs.softwaregrp.net'
certurl = url+seatid

headers = {

    'X-API-Key': prod_api,

    'Content-Type': "application/json"

    }

resp = requests.get(certurl, headers=headers)
print(resp.text)
print(resp.status_code)