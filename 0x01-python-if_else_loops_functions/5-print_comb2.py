#!/usr/bin/python3
j = 0
for i in range(0, 99):
    print("{}{}".format(j, i % 10), end=", ")
    if i % 10 == 9:
        j += 1
print(99)
