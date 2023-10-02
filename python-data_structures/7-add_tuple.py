#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    argca = len(tuple_a)
    argcb = len (tuple_b)
    if argca < 2:
        if argca == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if argcb < 2:
        if argcb == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])



            
        
        
