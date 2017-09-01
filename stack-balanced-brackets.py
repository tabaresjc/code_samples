# -*- coding: utf-8 -*-
import sys


fin = open("data/balanced-brackets/input04.txt", "r")


def raw_input():
    return fin.readline()


n = int(raw_input().strip())

OPEN_TAGS = '{[('
CLOSE_TAGS = '}])'

matching = {c: o for c, o in zip(CLOSE_TAGS, OPEN_TAGS)}

for _ in xrange(n):
    line = raw_input().strip()
    stack = []
    balanced = False
    for i in xrange(len(line)):
        c = line[i:i + 1]
        if c in OPEN_TAGS:
            if stack and stack[-1] in CLOSE_TAGS:
                balanced = False
                break
            stack.append(c)
        elif c in CLOSE_TAGS:
            if not stack:
                balanced = False
                break
            last_c = stack.pop()
            if last_c != matching[c]:
                balanced = False
                break
            balanced = True
    print "YES" if balanced else "NO"
