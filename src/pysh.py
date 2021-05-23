import os
import init.initsh

bin = "src/utils"

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
        elif command=="exit":
            exit()
        elif f"{command}.py" not in os.listdir(bin):
            print("Command not found")
            break
    

def getDir():
    dir = os.getcwd()
    return dir


def main():
    init.initsh.clearshell()
    while True:
        print(getDir()+"$")
        command = getCommand()
        parsed_command = parse(command)
        execCommand(parsed_command)
        
        

main()
