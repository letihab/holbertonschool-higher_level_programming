#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in names:
        if names[i][0] != '__' and names[i][1] != '__':
            print(names[i])
 

