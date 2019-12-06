import sys

f = open(sys.argv[1], "r")
polymer = f.readline()
units = set(polymer.lower())
min_polymer = polymer

def RemoveReactingUnitsAt(polymer, idx):
  next = idx + 1
  while idx >= 0 and next < len(polymer) and polymer[idx] == polymer[next].swapcase():
    idx -= 1
    next += 1
  polymer = polymer[0:idx+1] + polymer[next:]
  return (polymer, idx)

for unit in units:
  new_polymer = polymer[:].replace(unit.lower(),"")
  new_polymer = new_polymer.replace(unit.upper(),"")
  idx = 0
  while new_polymer and idx != len(new_polymer):
    new_polymer, idx = RemoveReactingUnitsAt(new_polymer, idx)
    idx += 1
  if len(min_polymer) > len(new_polymer):
    min_polymer = new_polymer

print(min_polymer, len(min_polymer))
