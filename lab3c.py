#!/usr/bin/env python3

def operate(number1, number2, operator):
    n1 = int(number1)
    n2 = int(number2)
    if operator == 'add':
        return n1 + n2
    elif operator == 'subtract':
        return n1 - n2
    elif operator == 'multiply':
        return n1 * n2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))