#!/usr/bin/python3
def uppercase(str):
    i = 32
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result = ord(char) - i
        else:
            i = 0
        print('{}'.format(chr(result), end=''))
print('')
