#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        return int(str(number)[-1]) * -1
    return int(str(number)[-1])
