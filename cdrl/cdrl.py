import expinterpreter
import re

def getfile(name):
    with open(name, "r") as f:
           lines = [line.replace('\n', '').lstrip() for line in tokenize(f.read(), ";")]
    lines = [item for item in lines if item]
    return lines

def tokenize(expression, character):
            result=[]
            cur=""
            nest=0
            quotes=False
            escaped=False
            for i in expression:
                if i == "(" or i == "{":
                    nest += 1
                    escaped=False
                if i == ")" or i == "}":
                    nest -= 1
                    escaped=False
                if i == '"' and not escaped:
                    quotes = not quotes
                    escaped=False
                if i == "\\":
                    escaped=True
                if i == character and nest==0 and not quotes:
                    result.append(cur)
                    cur = ""
                    escaped=False
                else:
                    cur += str(i)
                    escaped=False
            result.append(cur)
            return result

def run(filename):
    file = getfile(f"{filename}.cdrl")
    print(file)
    def runlines(code=file):
        def action(code):
            line = ""
            index = -1
            while not "end" in line:
                index += 1
                line = tokenize(code[index], " ")
                print(line)
        action(code=code)
    runlines()
    
run("test")