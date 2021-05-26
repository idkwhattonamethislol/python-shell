import json

def adduser():
    with open('src/init/data/data.json','r') as f:
        data=json.load(f)
    name = input("Who is new user?\n")
    if not name in data:
        data[name] = {}
        data[name]["password"] = input("Password: ")
    with open('src/init/data/data.json','w') as f:
        json.dump(data, f)

adduser()
