# -*- coding: utf-8 -*-
import sys
file = open("data/insertionsort2/input.txt", "r")


def raw_input():
    return file.readline()


n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))

i = 0
while i < n - 1:
    if ar[i] > ar[i+1]:
        j = i
        while (j >= 0) and ar[j] > ar[j + 1]:
            c = ar[j + 1]
            ar[j + 1] = ar[j]
            ar[j] = c
            j -= 1
    print " ".join(map(str, ar))
    i += 1
