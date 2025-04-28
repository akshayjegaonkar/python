import json
import csv
with open("file.txt",'r') as file:
    txt = file.read()
    print(txt)


with open("output.json",'r') as json_file:
    data = json.load(json_file)
    print(data)


with open("ouput.csv",'r') as csv_file:
    data = csv.reader(csv_file)
    for row in data:
        print(row)