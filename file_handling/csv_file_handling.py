import csv

data = [
    ["name","location","mobile"],
    ["akshay","pune",2434234],
    ["raj","mumbai",2576232],
    ["sar",'indor',64326835]
]

with open("ouput.csv",'w',newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)