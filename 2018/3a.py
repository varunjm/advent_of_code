import sys

fabric = [0 for x in range(1000*1000)] 

f = open(sys.argv[1], "r")

for claim in f.readlines():
  at = claim.find('@')
  comma = claim.find(',')
  colon = claim.find(':')
  by = claim.find('x')

  left_border = int(claim[at+2:comma])
  top_border = int(claim[comma+1:colon])
  length = int(claim[colon+2:by])
  width = int(claim[by+1:])

  for y in range(top_border, top_border+width):
    for x in range(left_border, left_border+length):
      fabric[x + 1000*y] += 1

print (len([ inch_sq for inch_sq in fabric if inch_sq > 1]))