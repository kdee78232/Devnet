import json
with open('json_example.json')as data:
    json_data=data.read()

json_dict=json.loads(json_data)

json_dict 

json_dict["interface"]["name"]="WAN"