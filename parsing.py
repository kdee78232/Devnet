#parsing comma seperated value (csv) data

import csv
routerfile=open('routerlist.csv')
routerreader=csv.reader(routerfile)
routerdata=list(routerreader)
routerdata[2]


#with statement
with open('routerlist.csv') as data:
    csv_list=csv.reader(data)
    for row in csv_list:
        device = row[0]
        location=row[2]
        ip=row[1]
        print(f" {device} is in {location.rstrip} and has IP {ip}")

#use input with with command to add data to csv file
import csv
print("This terminal is for entering information")
hostname = input("Please enter the hostname:\n >")
ip = input("Please ennter IP Address:\n>")
location=input("Please enter the device location:\n>")
router=[hostname,ip,location]
with open("routerlist.csv","a")as data:
    csv_writer=csv.writer(data,quoting=csv.QUOTE_ALL)
    csv_writer.writerow(router)

with open('routerlist.csv','r') as data:
    print(data.read())


