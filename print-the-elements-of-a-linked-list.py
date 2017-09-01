# -*- coding: utf-8 -*-

file = open("data/print-the-elements-of-a-linked-list/input07.txt", "r")


def raw_input():
    return file.readline()


n, m = map(int, raw_input().strip().split(' '))

arr = [long(0) for n in xrange(n+1)]

for i in xrange(m):
    a, b, k = map(long, raw_input().strip().split(' '))
    arr[a - 1] += k
    arr[b] -= k

sum = 0
max = 0
for i in xrange(n):
    sum += arr[i]
    if sum > max:
        max = sum

print max
