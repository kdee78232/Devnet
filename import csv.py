import csv
samplefile=open("routerlist.csv")
samplereader=csv.reader(samplefile)
sampledata=list(samplereader)

sampledata[0]



with open("routerlist.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        location = row[2]
        ip = row[1]
        print(f"{device} is in {location.rstrip()} and has IP {ip}.")
        
