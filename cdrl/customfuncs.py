import kernel
import ast
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
            return ast.literal_eval(args)[inp]
