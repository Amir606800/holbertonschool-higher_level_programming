#!/usr/bin/python3

def factorial(n):
    s = 1
    while n > 0:
        s = s * n
        n -= 1
    return s


def pascal_triangle(n):
    umumi = []
    for i in range(n):
        balaja = []
        for j in range(i + 1):
            balaja.append(factorial(i) // (factorial(j) * factorial(i - j)), end=" "))
        umumi.append(balaja)
    return umumi
