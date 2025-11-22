#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = 0
    for i in range(len(roman_string)-1):
        curr = roman_string[i]
        next = roman_string[i+1]
        if nums[curr] >= nums[next]:
            number += nums[curr]
        else:
            number -= nums[curr]
    if roman_string:
        number += nums[roman_string[-1]]
    return number
