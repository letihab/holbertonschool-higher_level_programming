#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - ord('a') + ord('A'))
        print('{:s}'.format(char), end='')
print('{}'.format(''))
