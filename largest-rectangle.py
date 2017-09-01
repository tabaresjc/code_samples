# -*- coding: utf-8 -*-
import sys


file = open("data/largest-rectangle/input.txt", "r")


def raw_input():
    return file.readline()


n = int(raw_input().strip())
h = map(int, raw_input().strip().split(' '))

stack = []
area = 0
i = 0
while i < n:
    if not stack or h[i] >= h[stack[-1]]:
        stack.append(i)
        i += 1
    else:
        top = stack.pop()
        if stack:
            a = h[top] * (i - top - 1)
        else:
            a = h[top] * i

        if a > area:
            area = a

while len(stack):
    top = stack.pop()

    if stack:
        a = h[top] * (i - top - 1)
    else:
        a = h[top] * i

    if a > area:
        area = a

print area
