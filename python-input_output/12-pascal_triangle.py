#!/usr/bin/python3
""" First create a factorial function please. """


def factorial(n):
    """ Just start with value s with default one then decrase everytime and multiplicate """
    if n == 0:
        return 1
    s = 1
    while n > 0:
        s = s * n
        n -= 1
    return s


""" Now we can start to write the pascal function """


def pascal_triangle(n):
    """ create an general list to contain small portions """
    if n <= 0:
        return []
    umumi = []
    for i in range(n):
        balaja = []
        for j in range(i + 1):
            balaja.append(factorial(i) // (factorial(j) * factorial(i - j)))
        umumi.append(balaja)
    return umumi
