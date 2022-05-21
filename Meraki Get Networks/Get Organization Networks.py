# Get Organization Networks
#Operation Id:getOrganizationNetworks
#Description:List the networks that the user has privileges on in an organization

import requests

url = "https://api.meraki.com/api/v1/organizations/681155/networks"

payload = None

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

response = requests.request('GET', url, headers=headers, data = payload)

print(response.text.encode('utf8'))