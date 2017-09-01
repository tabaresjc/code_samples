# -*- coding: utf-8 -*-
import sys
file = open("data/insertion-sort-advanced/input04.txt", "r")


def raw_input():
    return file.readline()


n = int(raw_input().strip())

for iterate in range(n):
    x = int(raw_input().strip())
    ar = map(long, raw_input().strip().split(' '))
    answer = 0L

    i = 1
    c = ar[0]

    while i < x:
        if c > ar[i]:
            answer += 1
            j = i
            while (j > 0) and ar[j] > ar[j - 1]:
                answer += 1
                j -= 1
        else:
            c = ar[i]

        i += 1

    print answer
