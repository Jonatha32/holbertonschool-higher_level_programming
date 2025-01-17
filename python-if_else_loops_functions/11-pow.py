#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return (1)
    elif b > 0:
        c = 1
        for _ in range(b):
            c *= a
        return (c)
    else:
        c = 1
        for _ in range(abs(b)):
            c *= a
        return 1 / c
