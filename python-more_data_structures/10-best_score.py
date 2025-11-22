#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    items = list(a_dictionary.items())
    max_key, max_val = items[0]
    for key, val in items[1:]:
        if val > max_val:
            max_val = val
            max_key = key
    return max_key
