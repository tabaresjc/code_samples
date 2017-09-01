# -*- coding: utf-8 -*-
import sys
file = open("data/links/input2.txt", "r")


def raw_input():
    return file.readline()


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def Delete(head, position):
    prev = None
    current = head

    for n in xrange(position):
        prev = current
        current = current.next

    if prev:
        prev.next = current

    return current


lines = int(raw_input().strip())
head = None
for a in xrange(lines):
    d, p = map(int, raw_input().strip().split(' '))
    head = InsertNth(head, d, p)

while head.next:
    print head.data
    head = head.next
print head.data
