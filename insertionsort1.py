# -*- coding: utf-8 -*-
import sys
file = open("data/insertionsort1/input02.txt", "r")


def raw_input():
    return file.readline()


m = int(raw_input().strip())
ar = [int(i) for i in raw_input().strip().split()]

n = m - 1
e = ar[n]

while n >= 0:
    if ar[n - 1] > e:
        ar[n] = ar[n - 1] if n > 0 else e
        print " ".join(map(str, ar))
    else:
        ar[n] = e
        e = ar[n - 1]
    n -= 1
