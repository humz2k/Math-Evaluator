from math import *

def evaluate(expression):
    expression = "a=" + expression
    ldict = {}
    exec(expression,globals(),ldict)
    a = ldict['a']
    return a

if __name__ == "__main__":
    a = "( 1 + 1 ) - ( 2 *-22 /(2 - (2**2)))"
    print(evaluate(a))
