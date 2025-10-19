import os
import expinterpreter
import cdrl
curdir = os.getcwd()

def getfile(name):
    fileopen = open(name, "r")
    return fileopen.read()

print("Welcome to Cider OS commandline\nUse ´help´ for a list of commands")
while True:
    cmdfull = input(f"{curdir}> ")
    cmd=cmdfull.split()
    match cmd[0]:
        case "help":
            print(getfile("help.txt"))
        case "echo":
            print(expinterpreter.interpret(" ".join(cmd[1:])))
        case "install":
            cdrl.run("install.cdrl", f'["{cmd[1]}"]')
        case "cdrl":
            cdrl.run(cmd[1], f'[{cmdfull.split(" ", 2)[2]}]')
