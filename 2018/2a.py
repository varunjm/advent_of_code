import sys
from collections import Counter

two_count = 0
three_count = 0

def count_repeated_characters(ID):
  global two_count
  global three_count

  if 2 in Counter(ID).values():
    two_count += 1
  if 3 in Counter(ID).values():
    three_count += 1

f = open(sys.argv[1], "r")
map(count_repeated_characters, f.readlines())

print(two_count * three_count)