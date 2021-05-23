import sys
import os

def ls():
    for file in os.listdir(os.getcwd()):
        print(file)
        
ls()
    

