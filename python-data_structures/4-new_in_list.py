#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    argc = len(my_list) - 1
    #!/usr/bin/python3
def new_in_list(my_list, idx, element):
    argc = len(my_list) - 1
    list_copy = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > argc:
        return my_list
    else:
        list_copy[idx] = element
    return list_copy
        