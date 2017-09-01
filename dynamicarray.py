# -*- coding: utf-8 -*-

file = open("data/dynamycarray/input01.txt", "r")


def raw_input():
    return file.readline()


size, queryNumber = map(int, raw_input().strip().split(' '))

# init sequence list
seq = [[] for n in xrange(size)]
lastAnswer = 0
for i in xrange(queryNumber):
    query, x, y = map(int, raw_input().strip().split(' '))
    index = (x ^ lastAnswer) % size
    if query == 1:
        seq[index].append(y)
    elif query == 2:
        lastAnswer = seq[index][y % len(seq[index])]
        print lastAnswer
