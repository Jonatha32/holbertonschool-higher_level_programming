#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            mayus = chr(ord(a) - 32)
        else:
            mayus = a
        print("{}".format(mayus), end="")
    print()
