import requests
import json

global common_name
api22 ='01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'
InternalRenewURL = 'https://pki-ws-rest.symauth.com/mpki/api/v1/certificate/'
serialnumber = '49482acda52ddbaa6a6720f919fb4c7a'
internalrevokepostfix = '/renew'
certurl = InternalRenewURL+serialnumber+internalrevokepostfix
certificateoid = '2.16.840.1.113733.1.16.1.5.3.5.1.1312805533'
#certificateoid = '2.16.840.1.113733.1.16.1.5.3.5.1.1298715434'
common_name = "swinfra.net"
sid = common_name
email = "christian.edlinger2@microfocus.com"
csr = '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'
smaxid = '9999'
comment = 'Approved'
given_name ='Christian'
surname = 'Edlinger'
comments = 'SMAXID: '+smaxid+' '+comment
payload ={
  "profile" : {
    "id" : certificateoid
  },
  "seat" : {
    "seat_id" : sid,
    "email" : email
  },
  "csr" : csr,
  "authentication" : {
    "auth_comments" : comments,
    "auth_first_name" : given_name
   }
}

payload_new = json.dumps(payload)
print(payload_new)
headers = {
    'X-API-Key': api22,
    'Content-Type': "application/json"
    }

resp = requests.post(certurl, data=payload_new, headers=headers)
print(resp.text)
print(resp.status_code)