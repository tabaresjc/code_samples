# -*- coding: utf-8 -*-
import sys
file = open("data/links/input.txt", "r")


def raw_input():
    return file.readline()


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def InsertNth(head, data, position):
    node = Node(data)

    if not head or position == 0:
        node.next = head
        return node

    current = head

    for n in xrange(position - 1):
        current = current.next

    node.next = current.next
    current.next = node

    return head


lines = int(raw_input().strip())
head = None
for a in xrange(lines):
    d, p = map(int, raw_input().strip().split(' '))
    head = InsertNth(head, d, p)

while head.next:
    print head.data
    head = head.next
print head.data
