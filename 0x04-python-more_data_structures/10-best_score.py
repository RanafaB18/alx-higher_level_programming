#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maximum = 0
        for key, value in a_dictionary.items():
            if value > maximum:
                maximum = value
                max_key = key
    else:
	 return None
    return max_key
