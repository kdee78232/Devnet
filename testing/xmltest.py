# pip install xmltodict# only needed if not installed

import xmltodict

with open("xml_example.xml")as data:
    xml_example=data.read()

xml_dict = xmltodict.parse(xml_example)

print(xml_dict)

xml_dict["interface"]["ipv4"]["address"]="10.10.1.1"

#view changes 
print(xmltodict.unparse(xml_dict,pretty=True))

#save changes write to file
with open("xml_example.xml","w")as data:
    data.write(xmltodict.unparse(xml_dict,pretty=True))

