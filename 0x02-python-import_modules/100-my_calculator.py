#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    numOfArgs = len(argv)
    if numOfArgs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = "+-*/"
    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} + {} = {}".format(a, b, a + b))
