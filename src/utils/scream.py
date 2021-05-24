"""This command is the equivalent of echo on unix"""
import sys

def scream():
    for i in range(0, len(sys.argv)):
        if i>0:
            print(str(sys.argv[i]), end=' ')
    print("\n")

scream()
