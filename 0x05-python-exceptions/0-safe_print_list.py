#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    newlist = ""
    try: 
        for i in range(x):
            newlist += str(my_list[i])
    except IndexError:
        pass
    return int(newlist)
