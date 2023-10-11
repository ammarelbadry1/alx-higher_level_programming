#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or not roman_string):
        return (0)
    romans = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    roman_string_len = len(roman_string)
    result = 0
    i = 0
    while (i < roman_string_len):
        current = romans[roman_string[i]]
        if (i + 1 < roman_string_len):
            next = romans[roman_string[i + 1]]
            if (current < next):
                result += next - current
                i += 2
            else:
                result += current
                i += 1
        else:
            result += current
            i += 1
    return (result)
