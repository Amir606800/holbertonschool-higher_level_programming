#!/usr/bin/python3
# 122- z
# 90 - Z
i = 122
num = 0

while num <= 25:
    k = i
    if (num % 2 == 1):
        k = i-32
    print("{}".format(chr(k)), end="")
    i -= 1
    num += 1
