import expinterpreter
import kernel
import ast

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
                elif not i == " " or cur != "":
                    cur += str(i)
                    escaped=False
            result.append(cur)
            return result

def run(filename,args):
    kernel.write("", "static____")
    file = getfile(filename)
    def runlines(code, args):
        line = " "
        index = -1
        while not line[0] == "end":
            index += 1
            line = tokenize(code[index], " ")
            if not line[0][0:2] == "//":
                match line[0]:
                    case "echo":
                        print(expinterpreter.interpret(line[1], args))
                    case "rep":
                        for i in range(int(expinterpreter.interpret(line[1], args))):     
                            runlines(tokenize(line[2][1:-1], ";"), args=args)
                    case "while":
                        while expinterpreter.interpret(line[1], args):     
                            runlines(tokenize(line[2][1:-1], ";"), args=args)
                    case "wipe":
                        kernel.wipe()
                    case "def":
                        kernel.write(line[2], line[1])
                    case "if":
                        if expinterpreter.interpret(line[1], args):
                            runlines(tokenize(line[2][1:-1], ";"), args=args)
                        elif len(line) > 3:
                            if line [3] == "else":
                                runlines(tokenize(line[4][1:-1], ";"), args=args)
                    case "var":
                        kernel.write(expinterpreter.interpret(line[2], args), expinterpreter.interpret(line[1], args))
                    case "varadd":
                        kernel.write(expinterpreter.interpret(f'("var":{line[1]})', args) + expinterpreter.interpret(line[2], args), expinterpreter.interpret(line[1], args))
                    case "call":
                        runlines(tokenize(expinterpreter.interpret(f'("var":"{line[1]}")', args)[1:-1], ";"), expinterpreter.interpret(line[2], args))
                    case "append":
                        arr = ast.literal_eval(expinterpreter.interpret(f'("var":{line[1]})', args))
                        arr.append(expinterpreter.interpret(line[2], args))
                        kernel.write(str(arr), expinterpreter.interpret(line[1], args))
                    case "writefile":
                        with open(expinterpreter.interpret(line[1], args), "w") as f:
                            f.write(expinterpreter.interpret(line[2], args))
                    case "cdrl":
                        run(expinterpreter.interpret(line[1], args), expinterpreter.interpret(line[2], args))

    runlines(file, args)

#run("cml.cdrl", '[]')
