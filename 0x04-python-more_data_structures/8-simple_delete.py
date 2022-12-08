#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key, 0) != 0:
        del a_dictionary[key]
    return a_dictionary
