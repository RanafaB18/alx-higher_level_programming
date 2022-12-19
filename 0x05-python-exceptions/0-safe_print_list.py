#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while (count < x):
            print(f"{my_list[i]}", end="")
            count = count + 1
            print(count)
        print()
    except IndexError:
        raise IndexError
    finally:
        return count
