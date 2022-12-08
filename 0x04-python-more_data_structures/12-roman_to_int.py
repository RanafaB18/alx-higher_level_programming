#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    total = 0
    roman_nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        value = roman_nums[roman]
        total += value if total < value * 5 else -value
    return total
