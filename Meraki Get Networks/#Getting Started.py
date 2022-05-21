#Getting Started
#If using the Meraki Python library, install it via  pip
#pip install meraki

#Base URI
# Every API request will begin with the following base URI. 
# https://api.meraki.com/api/v1

#Authorization
#The Meraki Dashboard API requires a header parameter of 
# #X-Cisco-Meraki-API-Key to provide authorization for each request.

#optional Export your API key as an environment variable, for example:
#



pip install meraki
import meraki
dashboard = meraki.DashboardAPI(API_KEY)

