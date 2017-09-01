# -*- coding: utf-8 -*-

file = open("data/array-left-rotation/input.txt", "r")


def raw_input():
    return file.readline()


n, d = map(int, raw_input().strip().split(' '))
arr = map(int, raw_input().strip().split(' '))

arr[:] = arr[d:] + arr[:d]
print " ".join(map(str, arr))
