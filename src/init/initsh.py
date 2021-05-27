import os
from time import sleep
import json

def getData():
    with open('src/init/data/data.json','r') as f:
        data = json.load(f)
    return data

def write(data):
    with open('src/init/data/data.json','w') as f:
        json.dump(data, f, indent=4)

def login():
    username = input("Who is using this py-shell session? ")
    data = getData()
    if username in data:
        passwd = input("Password: ")
        if data[username]["password"] == passwd:
            return username
        else:
            print("Wrong password, exiting shell")
            exit(1)
    else:
        print("No such user, exiting...")
        exit(1)

loggedin=None

def check():
    data = getData()
    if len(data)==0:
        os.system("python3 src/utils/adduser.py")
        loggedin=login()
    else:
        loggedin=login()
    return loggedin

def clearshell():
    print("""Welcome to the python shell. Use this shell without root privileges to avoid risks. See the github repo at https://github.com/idkwhattonamethislol/python-shell""")
    sleep(5.0)
    os.system("cls||clear")
