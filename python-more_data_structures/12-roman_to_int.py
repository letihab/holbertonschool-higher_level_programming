#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    else:
        roman_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                       'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for number in reversed(roman_string):
        current_value = roman_value.get(number, 0)
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
            prev_value = current_value
    return result
