import requests
import json
import sys
#from requests import api

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
prod_api = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
api = prod_api
# Order ID from SMAX
orderid = sys.argv[1]
revokeurl = 'https://www.digicert.com/services/v2/order/certificate/'
revokeurlpostfix = '/revoke'
url=revokeurl+orderid+revokeurlpostfix
# Justification from SMAX
justification = sys.argv[2]

payload = {
    "comments": justification,
    "skip_approval": "true",
}

payload_new = json.dumps(payload)
print(payload_new)
headers = {
    'X-DC-DEVKEY': api,
    'Content-Type': "application/json"
    }

response = requests.request("PUT", url, data=payload_new, headers=headers)
print(response.text)
print(response.status_code)