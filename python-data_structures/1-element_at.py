#!/usr/bin/python3
def element_at(my_list, idx):
    argc = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > argc:
        return None
    else:
        return my_list[idx]
