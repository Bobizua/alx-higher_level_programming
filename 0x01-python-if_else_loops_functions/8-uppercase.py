#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if(64 < ord(i) < 91):
            i = chr(ord(i) - 32)
            print("{}".format(i), end='')
            print()
