#!/usr/bin/python3
def uppercase(str):
    i = 0
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            i = 32
        else:
            i = 0:
        print('{:c}'.format(ord(char) - i), end='')
print('')
