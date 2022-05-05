import json
with open("GigabitEthernet2.json") as data:
    json_data=data.read

json_dict=json.loads(json_data)

print(json_dict)


json_dict["address"]["ip"]="192.168.10.1"

# use 0 to work with chained items i.e. "ip" to  change items.
 json_dict["interface"]["ipv4"]["address"][0]["ip"]="10.1.1.2"

In [12]: json_dict
Out[12]: 
{'interface': {'name': 'GigabitEthernet2',
  'description': 'Wide Area Network',
  'enabled': True,
  'ipv4': {'address': [{'ip': '10.1.1.2', 'netmask': '255.255.255.0'}]}}}


