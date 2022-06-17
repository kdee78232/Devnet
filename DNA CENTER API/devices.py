# website for API https://developer.cisco.com/docs/dna-center/#!devices/devices-api



import requests
from requests.auth import HTTPBasicAuth
#import urllib3 library and disable self-signed certificate error**do not use in production environment
import urllib3
urllib3.disable_warnings()

#Authentication

BASE_URL = 'https://<IP Address>'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = '<USERNAME>'
PASSWORD = '<PASSWORD>'

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
print(response.json()['Token'])



#Get Device Info
# 1 Authenticate Get Token
import requests
from requests.auth import HTTPBasicAuth
import urllib3
urllib3.disable_warnings()

BASE_URL = 'https://<IP Address>'
AUTH_URL = '/dna/system/api/v1/auth/token'
USERNAME = '<USERNAME>'
PASSWORD = '<PASSWORD>'

response = requests.post(BASE_URL + AUTH_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), verify=False)
token = response.json()['Token']
headers = {'X-Auth-Token': token, 'Content-Type': 'application/json'}

DEVICES_COUNT_URL = '/dna/intent/api/v1/network-device/count'
response = requests.get(BASE_URL + DEVICES_COUNT_URL, headers = headers, verify=False)
print(response.json())



# For devices enter code to get devices

DEVICES_URL = '/dna/intent/api/v1/network-device'
response = requests.get(BASE_URL + DEVICES_URL, headers = headers, verify=False)
#Print out list 
for item in response.json()['response']:
    print(item['id'], item['hostname'], item['managementIpAddress'])








