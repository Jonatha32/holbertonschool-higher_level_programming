#!/usr/bin/python3
def max_integer(my_list=[]):
    a = len(my_list)
    if my_list == "":
        return (a, None)
    mayor = my_list[0]

    for i in my_list:
        if i > mayor:
            mayor = i

    return (mayor)
