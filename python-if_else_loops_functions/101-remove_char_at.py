#!/usr/bin/python3

def remove_char_at(str, n):
    _str = ''
    for i in str:
        if int(i) < 0:
            _str = str
        elif i != n:
            _str = str[:n] + str[n+1:]
    return _str


# print(remove_char_at("qwerty", -2))
