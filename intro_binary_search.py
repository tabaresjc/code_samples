# -*- coding: utf-8 -*-
import sys
file = open("data/insertionsort2/input.txt", "r")


def raw_input():
    return file.readline()


v = int(raw_input().strip())
n = int(raw_input().strip())
ar = [int(i) for i in raw_input().strip().split()]

factor = 1
pos = n - 1
while True:
    if n / (factor * 2) > 0:
        factor *= 2
        incf = n / factor
    else:
        incf = 1

    if ar[pos] == v:
        break
    elif ar[pos] > v:
        pos -= incf
    else:
        pos += incf

print pos
