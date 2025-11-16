#!/usr/bin/python3
# 122- z
# 90 - Z
i = 122
num = 0
while num <= 25:
    if (num % 2 == 1):
        print(chr(i-32), end="")
    else:
        print(chr(i), end="")
    i-=1
    num+=1
