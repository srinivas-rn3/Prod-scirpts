import requests
import json
import sys

global common_name
#api22 ='01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'
prod_api = '017d1f0298ca0b9c02_89F736A27B08E31A6919E8DC72F54DC69F5B53C6D0B0E7690564A50D6A4D976A'
InternalRevokeURL = 'https://pki-ws-rest.symauth.com/mpki/api/v1/certificate/'

# Serial Number from SMAX
serialnumber = sys.argv[1]
internalrevokepostfix = '/revoke'
certurl = InternalRevokeURL+serialnumber+internalrevokepostfix

# Justification from SMAX
justification = sys.argv[2]

payload ={
    "revocation_reason" : justification
}

payload_new = json.dumps(payload)
#print(payload_new)
headers = {
    'X-API-Key': prod_api,
    'Content-Type': "application/json"
    }

resp = requests.put(certurl, data=payload_new, headers=headers)
print(resp.text)
print(resp.status_code)