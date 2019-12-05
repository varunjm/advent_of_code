import sys
from collections import Counter

substrings = dict()
match=""

def count_repeated_characters(ID, idx):
  global match
  for i in range(0, len(ID)-1):
    sub = ID[:i] + ID[i+1:]
    if sub in substrings and substrings[sub][0] != idx:
      match = sub
      return True
    substrings[sub] = (idx, i)
  return False

f = open(sys.argv[1], "r")

any(count_repeated_characters(ID, idx) for idx, ID in enumerate(f.readlines()))
print(match)