import json
with open("GigabitEthernet2.json") as data:
    json_data=data.read

json_dict=json.loads(json_data)

print(json_dict)


json_dict["address"]["ip"]="192.168.10.1"



