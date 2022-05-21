pip install requests

import requests
url = "https://postman-echo.com/post"
payload = "This is New"
headers={'content-type':"text/plain"}
response=requests.request("POST",url,data=payload,headers=headers)
print(response.text)