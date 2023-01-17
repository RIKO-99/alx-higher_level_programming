#!/usr/bin/python3
for i in range (1,9):
    for j in range (1,9):
        if(i != j):
             print("{:d}{:d}".format(i, j), end=", ")
