#!/usr/bin/python3
def roman_to_int(roman_string):
    sum_of_int = 0
    roman_nums = {
                  "I": 1, "V": 5, "X": 10, "L": 50, (\)
                  "C": 100, "D": 500, "M": 1000 (\)
                 }
    length = len(roman_string)
    if length == 1:
        return roman_nums.get(roman_string)
    for i in range(0, length):
        curr = roman_string[i]
        sum_of_int += roman_nums.get(curr)
        if i + 1 < length:
            next_char = roman_string[i + 1]
            if curr == "I" and next_char and next_char != "I":
                sum_of_int -= 2
    return sum_of_int
