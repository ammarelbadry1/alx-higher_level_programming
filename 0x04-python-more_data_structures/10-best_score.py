#!/usr/bin/python3
def best_score(a_dictionary):
    if (not a_dictionary):
        return None
    best = list(a_dictionary.keys())[0]
    for i in a_dictionary:
        if a_dictionary[i] > a_dictionary[best]:
            best = i
    return (best)
