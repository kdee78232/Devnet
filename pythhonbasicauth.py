import requests
url="https://postman-echo.com/basic-auth"
headers={
    'authorization':"Basic cG9zdG1hbjpwYXNzd29ya=="

}
response=requests.request("GET",url,headers=headers)
print(response.text)
#use for basic authorization for GET request#


#import requests
    ...: url="https://postman-echo.com/basic-auth"
    ...: headers={
    ...:     'authorization':"Basic cG9zdG1hbjpwYXNzd29ya=="
    ...: 
    ...: }
    ...: response=requests.request("GET",url,headers=headers)
    ...: print(response.text)
    ...: 
Unauthorized

