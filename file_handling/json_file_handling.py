import json

data = {
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}

with open("output.json",'w') as file:
    json.dump(data,file,indent=4)
