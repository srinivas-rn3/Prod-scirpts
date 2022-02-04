import requests
import json
import sys

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api_prod = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
api = api_prod

certificateid = sys.argv[1]
url = "https://www.digicert.com/services/v2/certificate/"+certificateid+'/sendemail'
email = sys.argv[2]
email2 = sys.argv[3]

payload = {
  "emails": [
      email,
      email2
      ],
  "certificate_collect_format": "downloadlink",
  "custom_message": "Please install this certificate!"
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