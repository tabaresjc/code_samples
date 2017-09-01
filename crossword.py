
lines = [
  "+-++++++++",
  "+-++++++++",
  "+-------++",
  "+-++++++++",
  "+-++++++++",
  "+------+++",
  "+-+++-++++",
  "+++++-++++",
  "+++++-++++",
  "++++++++++",
]

words = "AGRA;NORWAY;ENGLAND;GWALIOR".split(";")

# lines = []
# for n in xrange(10):
#     lines.append(raw_input().strip())
#
# words = raw_input().strip().split(";")

vert, horiz = {}, {}
len_words = sorted(map(len, words))
min_len = len_words[0]

n = 0
for x in xrange(10):
    tot = sum([1 for c in list(lines[x]) if c == "-"])
    if tot >= min_len:
        horiz[x] = tot

transp_lines = [list(i) for i in zip(*lines)]
for y in xrange(10):
    tot = sum([1 for c in list(transp_lines[y]) if c == "-"])
    if tot >= min_len:
        vert[y] = tot

print vert
print horiz
