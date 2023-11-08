#!/usr/bin/python3
import hidden_4

words = dir(hidden_4)
for word in words:
    if word[0:2] != '__':
        print(word)
