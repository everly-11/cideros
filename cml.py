import os
import expinterpreter
curdir = os.getcwd()

def getfile(name):
    fileopen = open(name, "r")
    return fileopen.read()

print("Welcome to Cider OS commandline\nUse ´help´ for a list of commands")
while True:
    cmd=input(f"{curdir}> ").split()
    match cmd[0]:
        case "help":
            print(getfile("help.txt"))
        case "echo":
            print(expinterpreter.interpret(" ".join(cmd[1:])))