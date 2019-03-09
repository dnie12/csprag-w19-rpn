#!/usr/bin/env python3

import operator


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '&': operator.and_,
    '|': operator.or_,
    '~': operator.invert,
    '//': operator.floordiv,
}

def factorial(arg1):
    value = arg1
    arg1 -= 1
    while(arg1 > 0):
        value *= arg1
        arg1 -= 1
    return value

def percentage(arg1, arg2):
    value = arg1
    value = arg1 * arg2/100
    return value


def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            if token is '!':
                arg1 = stack.pop()
                result = factorial(arg1)
                stack.append(result)
            elif token is '%':
                arg2 = stack.pop()
                func = stack.pop()
                arg1 = stack.pop()
                function = operators[func]
                arg2 = percentage(arg1, arg2)
                result = function(arg1, arg2)
                stack.append(result)
            elif len(stack) is 1 and token is not '~':
                stack.append(token)
            else:
                function = operators[token]
                if token is '~':
                    arg1 = stack.pop()
                    result = function(arg1)
                    stack.append(result)
                else:
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    result = function(arg1, arg2)
                    stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
