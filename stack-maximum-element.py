# -*- coding: utf-8 -*-
import sys
file = open("data/maximum-element/input12.txt", "r")


def raw_input():
    return file.readline()


n = int(raw_input().strip())
stack = []
max_val_stack = [1]

for _ in xrange(n):
    cmd, val = ((raw_input().strip() + " 0").split(' '))[:2]
    if cmd == '1':
        val = long(val)
        stack.append(val)
        if val >= max_val_stack[-1]:
            max_val_stack.append(val)
    elif cmd == '2':
        val = stack.pop()
        if max_val_stack[-1] == val:
            max_val_stack.pop()
    elif cmd == '3':
        print max_val_stack[-1]
