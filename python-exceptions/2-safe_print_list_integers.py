#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for idx in range(x):
            if isinstance(my_list[idx], int):
                print("{:d}".format(my_list[idx]), end='')
                printed += 1
    except (ValueError, TypeError, IndexError):
        pass
    print()
    return (printed)
