
"""USE THIS SHELL AT YOUR OWN RISK. USE WITH SUDO/ADMIN PRIVILEGES IS NOT ADVISED"""

import os
from init.initsh import check, clearshell

bin = "src/utils"

def pwd():
    dir = os.getcwd()
    print("Current working directory: "+dir)

def parse(command):
    parsed = command.split(" ")
    return parsed

def getCommand():
    command = input()
    return command

def execCommand(parsed:list):
    command = parsed[0]
    for file in os.listdir(bin):
        if file == f"{command}.py" and len(parsed)>1:
            os.system(f"python3 {bin}/{command}.py {''.join(f'{parsed[1:]}')}")
        elif file==f"{command}.py" and len(parsed)==1:
            os.system(f"python3 {bin}/{command}.py")
        elif command=="pwd":
            pwd()
            break
        elif command == "exit":
            exit(0)
        elif command == None:
            pass
        elif f"{command}.py" not in os.listdir(bin):
            print("Command not found")
            break
        
    

def getDir():
    dir = os.getcwd()
    return dir

def main():
    clearshell()
    loggedinuser = check()
    while True:
        print(getDir()+"&user={}:$".format(loggedinuser),end=' ')
        command = getCommand()
        parsed_command = parse(command)
        execCommand(parsed_command)
        
        

main()
