#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    else:
        dictionary = {'I' :1, 'V': 5, 'X': 10, 'XV': 15, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
    result = 0
    prev_value = 0
    for number in reversed(roman_string):
        current_value = dictionary[number]
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
            prev_value = current_value
        return result

    