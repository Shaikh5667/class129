import csv

dataSet_1 = []
dataSet_2 = []

with open("final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataSet_1.append(row)


with open("archive_dataset.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataSet_2.append(row)

header_1 = dataSet_1[0]
planet_data__1 = dataSet_1[1]

header_2 = dataSet_2[0]
planet_data__2 = dataSet_2[1]

headers = header_1 , header_2
planet_data = []
for index, data_row in enumerate(planet_data__1):
    planet_data.append(planet_data__1[index]+planet_data__2[index])

with open("margedataset.csv","a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)



