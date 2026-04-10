#!/usr/bin/python3
def uppercase(str):
    for index in range(len(str)):
        if ord(str[index]) >= 97 and ord(str[index]) <= 122:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[index]) - num), end='')
    print()
