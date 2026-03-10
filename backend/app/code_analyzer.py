import ast

def basic_syntax_check(code):

    try:
        ast.parse(code)
        return "Syntax is valid"
    except Exception as e:
        return f"Syntax Error: {e}"
