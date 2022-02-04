import requests
import json
import sys
#from requests import api

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api_prod = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
api = api_prod

#url = "https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex"

email = sys.argv[1]
common_name = sys.argv[2]
#externalcsr = 'MIIDDTCCAfUCAQAwgYoxCzAJBgNVBAYTAkdCMRIwEAYDVQQIEwlCZXJrc2hpcmUxEDAOBgNVBAcTB05ld2J1cnkxCzAJBgNVBAsTAklUMSYwJAYDVQQKEx1NaWNybyBGb2N1cyBJbnRlcm5hdGlvbmFsIHBsYzEgMB4GA1UEAxMXc2VydmVyMS5lYXN0YmF5Y2FmZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDRBsaGEktC/9ruokg8LcBihNOS1/aOpnWEUtQ946wsDlvDO86ClrhUurOE6EDbRTcqEPlAmFOYjqBcEJBeZ1VzH/6xdvcDcNfACLbXCk6i2/sjfodXMAs24UEmuFGFj5XOdl5mc5Fcpztfumg0Ck0aTsuAOSrx8GxN8/DrGKAsiVTTX/NLI3OuagsLOCmhUhcKEhh9cI1E1WQxzwMQcCXhVb5V4e+UeAbcw9wWPpR6DsVP76stEfKzmXkIqWpgRCxr63Z4LhxWXiXI+7XezhEBsdfGgXYUBnDdQsmLVq5+gAsDN3YM7HiKusEe4/5vK8Rl2CsnJpYis/MGwaf3nJlpAgMBAAGgPTA7BgkqhkiG9w0BCQ4xLjAsMCoGA1UdEQQjMCGCH2h0dHBzOi8vc2VydmVyMS5lYXN0YmF5Y2FmZS5jb20wDQYJKoZIhvcNAQEFBQADggEBALFzHY0Ruu0PBEyQIKH72Ze2YED1Hts2kbspraZBRxh6zPe32/O4WdP5o3155jKNTl/YqREbC9x+zFbVYWHpwdagXpWmcTkjlEU8p0/faL3Qyl3QTQ3UNRGFR05OAI6Qqwq14VkLwcUmowMcnTtMeL1Iig/jY4UcNv6Ruc74fTiY39ZuhuISVqwlmFOV/qW6MjP1xt/YYaZlObNaBoKYP80JxsE3IUK3J/7yfA2SOzj5zGeH2oetn/7SSev7ol9aIFOvvBmi88AyllJYyvqpisQbAi6Fy5rlvyqVpYZHGzDjtqhPntB41UvLcQ+xB+XRYCU0VHMYb83cBEip52vdGcE='
externalcsr = sys.argv[3]
given_name = sys.argv[4]
surname = sys.argv[5]
name = given_name+' '+surname
san1 = sys.argv[6]
if san1 == '':
    san1 = common_name
smaxid = sys.argv[7]
comment = sys.argv[8]
comments = "SMAX Ref:"+smaxid+' - '+comment
#External_Cert_Type = "dev" 
external_cert_type = sys.argv[9]
if external_cert_type == "Basic OV":
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_basic'
elif external_cert_type == "Basic EV":
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_ev_basic'
else:
    url = 'https://www.digicert.com/services/v2/order/certificate/ssl_securesite_flex'

payload = {
    "certificate": {
        "common_name": common_name,
        "dns_names": [
            san1
        ],
        "csr": externalcsr,
        "signature_hash": "sha256",
    },
    "comments": comments,
    "container": {
        "id": 562528
    },
    "skip_approval": "false",
    "auto_renew": 0,
    "organization": {
        "id": 41411,
                "contacts": [
            {
                "contact_type": "ev_approver",
                "user_id": 2457134  
            },
            {
                "contact_type": "technical_contact",
                "first_name": given_name,
                "last_name": surname,
                "email": email
            }
        ]
    },
    "order_validity": {
      "days": 365
    },
    "payment_method": "balance"
}

payload_new = json.dumps(payload)
#print(payload_new)
headers = {
    'X-DC-DEVKEY': api,
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload_new, headers=headers)
#print(response.text["id"])
resp_dict = json.loads(response.text)
print(str(resp_dict["id"])+"is the certificate id")
print(response.status_code)