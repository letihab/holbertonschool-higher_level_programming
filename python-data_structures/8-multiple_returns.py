#!/usr/bin/python3
def multiple_returns(sentence):
    argc = len(sentence)
    if argc == 0:
        return (0, None)  
    else:      
        return argc, sentence[0]
