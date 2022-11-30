#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        ascii_num = ord(i)
        # Check if it's lowercase
        # In range for uppercasing
        if ascii_num > 96 and ascii_num < 123:
            new_string += chr(ord(i) - 32)
            continue
        new_string += i
    print(new_string)
