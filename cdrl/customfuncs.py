import kernel
import ast
import os
import expinterpreter
def func(action, inp, args):
    match action:
        case "str":
            return str(inp)
        case "int":
            return int(inp)
        case "float":
            return float(inp)
        case "bool":
            return (inp == "True") if inp in ("True", "False") else bool(inp)
        case "input":
            return input(inp)
        case "var":
            return kernel.get(inp)
        case "not":
            return not (inp == "True") if inp in ("True", "False") else bool(inp)
        case "arg":
            try:
                return ast.literal_eval(args)[inp]
            except IndexError:
                print("missing argument")
                print("attempted to find arg", inp, "in", args)
        case "request":
            return kernel.request(inp)
        case "getfile":
            return kernel.getfile(inp)
        case "oswdraw":
            return os.getcwd()
        case "eval":
            return expinterpreter.interpret(inp, args)
        case "len":
            return len(inp)
