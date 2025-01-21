#!/usr.bin/python3
def no_c(my_string):
    copy_list = []
    for i in range(len(my_string)):
        if my_string[i] != 'C' and my_string[i] != 'c':
            copy_list.append(my_string[i])
    return ''.join(copy_list)

