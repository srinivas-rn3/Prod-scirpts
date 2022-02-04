import requests
import json
import sys

global common_name
#api22 ='01e9cf13d8a92b0a51_1DD829BE79FC2C6DB1412B1F85C836833E947348E59D717717D0C3286D3CE839'
prod_api ='017d1f0298ca0b9c02_89F736A27B08E31A6919E8DC72F54DC69F5B53C6D0B0E7690564A50D6A4D976A'
certurl = 'https://pki-ws-rest.symauth.com/mpki/api/v1/certificate'
# Email retrived from SMAX
email = sys.argv[1]
# Common Name retrived from SMAX
common_name = sys.argv[2]
#common_name = "mc4w01851.itcs.softwaregrp.net"
sid = common_name
#country = "GB"
#locality = "Berkshire"
#organisationname = "Micro Focus International plc"
#department = "IT"
#csr = 'MIIDDTCCAfUCAQAwgZExCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEnMCUGA1UEAxMebWM0dzAxODUxLml0Y3Muc29mdHdhcmVncnAubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvATAqwt/IaU+UKZCHbGy2RZ15keGktP83YlEN5uupqh2SMeF0LqRcGZXsEbTIeM/fS44GEk/BdNYaucY0jEA39JTERWWpyzjPJL968+mPSNwg7YEcUtwWKTUgbxaDpEyuc8KfT/+g70yCryAfAJnx4G24izyiAZWQMoQ10uMs4QyT1oL6TFF0bGj0rAXsoQhQ1MpKOvx/DTUavnloXILLMBTk3OR7lqWmB+JB8EA3kQsKb31LrBxhHY2c4CTJ0bvdwmdkCttyvMHwWnJad4Fa60VDpj6X6gnFueLUHmEg7aMVASrF+4TtiRVgnzYtwofvrM6wUqfs5A7SoCrsGWX5QIDAQABoDYwNAYJKoZIhvcNAQkOMScwJTAjBgNVHREEHDAaghhtYzR3MDE4NTEubWljcm9mb2N1cy5jb20wDQYJKoZIhvcNAQEFBQADggEBAF/kOIR1wxN2qlrf0+owUVGdl0fDfA/pXeFh80BfQpfZkAZI4vbAr2pztxG5xoBO1/sWuEdIr5QyM06EXwn8AM+z+DuibyyHTocFnvqWeM8wqkFo6pMwc/5OHFuUAJKX8QpqeYQKhCLh0BdxOIbZTCTAst7LMQjgPGRdTAkZqI2Vjk3n99LlhEf/K8GmhH2j3xfwITlEDoMcLAlu6chfp5D2afFIpF3m/IiRPO4GSaUKpM6XqgpbWtQKSUTZ0fZ6PbbyefqOnf703IRFlbhZ8xm+XRX7I6QWUEYEEyEMx4rrHi6KLUcAHKxkfwiEjgGk7FRLmxSsoNGwl4hrPSCd73c='
# CSR retrived from SMAX
csr = sys.argv[3]
#certificateoid = "2.16.840.1.113733.1.16.1.5.2.5.1.1279460975"
certificateoid = '2.16.840.1.113733.1.16.1.5.3.1.1.483560546'
profilename =  "SSL"
#duration = "10"
#validityunit = "Days"
# Given Name retrived from SMAX
given_name = sys.argv[4]
# Surname retrived from SMAX
surname = sys.argv[5]
# SAN1 retrived from SMAX
san1 = sys.argv[6]
#if san1 == '':
#  san1 = common_name
#SMAX ID retrieved from SMAX
smaxid = sys.argv[7]
#comments retrieved from SMAX
comment = sys.argv[8]
comments = "SMAX Ref:"+smaxid+' - '+comment

#san1 = "mc4w01851.microfocus.com"
payload ={
  "attributes": {
    "common_name": common_name,
    "dnsName":common_name,
    "given_name":given_name,
    "surname":surname,
    "custom_encode_dnsName":common_name,
    "custom_encode_dnsName_multi":san1
    },
    "email": email,
  "csr": csr,
  "profile": {
    "id": certificateoid,
    "name": profilename
  },
  "seat": {
    "email": email,
    "seat_id": common_name,
    "seat_name": common_name
  },
  "authentication" : {
    "auth_comments" : comments,
    },
}

payload_new = json.dumps(payload)
#print(payload_new)
headers = {
    'X-API-Key': prod_api,
    'Content-Type': "application/json"
    }

resp = requests.post(certurl, data=payload_new, headers=headers)
print(resp.text)
print(resp.status_code)