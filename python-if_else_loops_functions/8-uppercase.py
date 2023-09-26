#!/usr/bin/python3
def uppercase(str):
    result = 0
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result = ord(char) - 32
        else:
            result = ord(char)
        print("{}".format(chr(result)), end="")
    print('')
