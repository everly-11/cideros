import re
import customfuncs

def interpret(expr, args):
    def tokenize(expression):
        token_pattern = r'"(?:[^"\\]|\\.)*"|[+\-*/():=<>\[\]]|\d+\.\d+|\d+'
        tokens = re.findall(token_pattern, expression)
        tokens = [t.replace('\\"', '"') for t in tokens]
        return tokens
    def parse_expression(index, tokens):
        values = []
        ops = []

        def apply_operator():
            right = values.pop()
            left = values.pop()
            op = ops.pop()
            if op == '+':
                if isinstance(left, bool) and isinstance(right, bool):
                    values.append(left and right)
                else:
                    values.append(left + right)
            elif op == '-':
                    values.append(left - right)
            elif op == '*':
                if isinstance(left, list) and isinstance(right, str):
                    values.append(right.join(map(str, left)))
                elif isinstance(left, bool) and isinstance(right, bool):
                    values.append(left or right)
                else:
                    values.append(left * right)
            elif op == '/':
                if isinstance(left, str) and isinstance(right, str):
                    values.append(left.split(right))
                else:
                    values.append(left / right)
            elif op == ':':
                values.append(customfuncs.func(left, right, args))
            elif op == '=':
                values.append(left == right)
            elif op == '<':
                if isinstance(left, bool) and isinstance(right, bool):
                    values.append(left <= right)
                else:
                    r = right.strip('"')
                    if ':' in r:
                        parts = r.split(':')
                        values.append(left[slice(*[int(x) if x else None for x in parts])])
                    else:
                        values.append(left[int(r)])
            elif op == '>':
                values.append(left >= right)
        precedence = {'+': 1, '-': 1, '*': 1, '/': 1, ':': 1, '=': 1, '<': 1, '>': 1, }

        while index < len(tokens):
            token = tokens[index]
            if token.isdigit() or re.match(r'^\d+\.\d+$', token):
                values.append(float(token) if '.' in token else int(token))
                index += 1
            elif token.startswith('"') and token.endswith('"'):
                values.append(token[1:-1])
                index += 1
            elif token in precedence:
                while (ops and ops[-1] in precedence and
                       precedence[ops[-1]] >= precedence[token]):
                    apply_operator()
                ops.append(token)
                index += 1
            elif token == '(':
                index, value = parse_expression(index + 1, tokens)
                values.append(value)
            elif token == ')':
                break
            else:
                raise ValueError(f"Unexpected token: {token}")

        while ops:
            apply_operator()

        return index + 1, values[0]
    tokens = tokenize(expr)
    result = parse_expression(0, tokens)[1]
    return result

#print(interpret('"hello"<"1,-1"', []))
