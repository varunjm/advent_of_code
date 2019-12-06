import sys

f = open(sys.argv[1], "r")
polymer = f.readline()

def RemoveReactingUnitsAt(polymer, idx):
  next = idx + 1
  while idx >= 0 and next < len(polymer) and polymer[idx] == polymer[next].swapcase():
    idx -= 1
    next += 1
  polymer = polymer[0:idx+1] + polymer[next:]
  return (polymer, idx)

idx = 0
while polymer and idx != len(polymer):
  polymer, idx = RemoveReactingUnitsAt(polymer, idx)
  idx += 1

print(polymer, len(polymer))
