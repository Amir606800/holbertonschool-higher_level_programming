#!/usr/bin/python3
def add_tuple(tuple_a=(1, 4), tuple_b=(3)):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
print(add_tuple())
