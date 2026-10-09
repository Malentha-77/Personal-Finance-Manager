import json

with open("finances.json", "r") as file:
    finances = json.load(file)

print(finances)