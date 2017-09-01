# -*- coding: utf-8 -*-

file = open("data/sparse-arrays/input.txt", "r")


def raw_input():
    return file.readline()


a = int(raw_input().strip())
words = []
for n in xrange(a):
    words.append(raw_input().strip())

b = int(raw_input().strip())

for n in xrange(b):
    query = raw_input().strip()
    print sum([1 for w in words if w == query])
