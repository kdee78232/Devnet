
import requests
url="https://postman-echo.com/get"
querystring={"test":"123"}
headers={}
response=requests.request("GET",url,headers=headers,params=querystring)
print(response.text)

#to add HTTP headers to a request, you can simply pass \n
#  them in a Python dict to the headers
#parameter. Similarly, you can send your own cookies to a \n 
# server by using a dict passed to the
#cookies parameter. Example 7-12 shows a simple \n 
# Python script that uses the Requests library
#and does a GET request to the Postman Echo server.
