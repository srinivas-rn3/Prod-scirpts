import requests
import json
import sys
import time
import datetime

#apiuser = 'BQ22EV4YY4ZX6P457IXHVIWH4PG7ET3H7QJIC4ZFQS4OIJ2EAAIEXWXCCVH3KK7LPFSPPVQCTOKRL45B6'
api_prod = 'BUAG35UKW24EWU6CGBICX4JEFNONQUDXRXXLHWE76ZE4KM3CDKVOHFU3EZTK6JZLVBLYP6KN3Z7BCK5MD'
api = api_prod
orderid = sys.argv[1]
url = 'https://www.digicert.com/services/v2/order/certificate/'+orderid

headers = {
    'X-DC-DEVKEY': api,
    'Content-Type': "application/json"
    }

response = requests.request("GET", url, headers=headers)
#print(response.text)
resp_dict = json.loads(response.text)
#print(resp_dict)
date_time = resp_dict["certificate"]["valid_till"]
pattern = '%Y-%m-%d'
datem = datetime.datetime.strptime(date_time, pattern)
Day = datem.day
Month = datem.month
Year = datem.year
epoch = int(time.mktime(time.strptime(date_time, pattern)))*1000
print("certificate id:"+str(resp_dict["certificate"]["id"])+",Serial Number:"+str(resp_dict["certificate"]["serial_number"])+",Valid till:"+str(epoch)+",Name:"+resp_dict["certificate"]["ca_cert"]["name"]+",Day:"+str(Day)+",Month:"+str(Month)+",Year:"+str(Year))
print(response.status_code)