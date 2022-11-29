#!/usr/bin/python3
def islower(c):
    ascii_num = ord(c)
    if ascii_num > 96 and ascii_num < 123:
        return True
    return False
