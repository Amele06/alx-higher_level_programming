#!/usr/bin/python3
for num in range(9):
    for j in range(num + 1, 10):
        if num * 10 + j < 89:
            print("{:d}{:d}".format(num, j), end=", ")
print("{:d}".format(89))
