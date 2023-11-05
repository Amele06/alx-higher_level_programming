#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for elements in my_string:
        if elements not in ("c", "C"):
            new_string += elements
            return new_string
