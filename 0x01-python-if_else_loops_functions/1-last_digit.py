#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if last_digit > 5:
    last_text = "and is greater than 5"
elif last_digit == 0:
    last_text = "and is 0"
else:
    last_text = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {last_text}")
