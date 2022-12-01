#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    numOfArgs = len(args) - 1
    arguments = "argument" if numOfArgs == 1 else "arguments"
    dot_colon = "." if numOfArgs == 0 else ":"
    print("{} {}{}".format(numOfArgs, arguments, dot_colon))
    if (numOfArgs > 0):
        for i in range(1, numOfArgs + 1):
            print("{}: {}".format(i, args[i]))
