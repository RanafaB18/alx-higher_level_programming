#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    numOfArgs = len(argv)
    if numOfArgs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = "+-*/"
    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator_funcs = [add, sub, mul, div]
    func = operator_funcs[operators.index(operator)]
    print("{} {} {} = {}".format(a, operator, b, func(a, b)))
