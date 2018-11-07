#!/usr/bin/env python3

import operator
from termcolor import colored

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()

            result = function(arg1, arg2)
            if token == '+':
                print(colored(arg1, 'green'), colored(token + arg2, 'green'))
            elif token == '-':
                print(colored(arg1, 'green'), colored(token + arg2, 'red'))
            elif token == '*':
                print(colored(arg1, 'green'), colored(token + arg2, 'green'))
            elif token == '/':
                print(colored(arg1, 'green'), colored(token + arg2, 'red'))
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def oi():
    print("this be poppin")

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
