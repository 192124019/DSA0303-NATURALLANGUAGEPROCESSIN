#18.Implement a simple FOPC parser for basic logical expressions using python program.
def FOPC(expr):
    # base cases
    if expr == "1":
        return True
    elif expr == "0":
        return False
    # recursion cases
    elif "!" in expr:
        return not FOPC(expr[2:])
    elif "|" in expr:
        return FOPC(expr[:2]) or FOPC(expr[3:])
    elif "&" in expr:
        return FOPC(expr[:2]) and FOPC(expr[3:])

# testing the FOPC parser with various logical expressions

expr = "(1&0) | (!(1|0))"
print("Expression:", expr)
print("Output:", FOPC(expr))

expr = "(!0) & (!1))"
print("\nExpression:", expr)
print("Output:", FOPC(expr))
