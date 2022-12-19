#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while (count < x):
            print(f"{my_list[count]}", end="")
            count = count + 1
    except IndexError:
        raise IndexError
    finally:
        print()
        return count
