#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for str in my_string:
        if str != 'c' and str != 'C':
            result += str
    return result
