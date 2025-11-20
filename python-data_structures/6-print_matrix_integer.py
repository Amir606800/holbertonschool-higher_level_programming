#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            print("{:d}".format(j), end="")
            if j < len(i) - 1:
                print("{:d}".format(j), end=" ")
        print()
