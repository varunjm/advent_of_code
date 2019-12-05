import sys

fabric = [0 for x in range(1000*1000)] 

f = open(sys.argv[1], "r")
unclaimed_list = set()
claims = f.readlines()
claim_list = []

#count first
for claim in claims:
  at = claim.find('@')
  comma = claim.find(',')
  colon = claim.find(':')
  by = claim.find('x')
  claim_number = int(claim[1:at-1])
  left_border = int(claim[at+2:comma])
  top_border = int(claim[comma+1:colon])
  length = int(claim[colon+2:by])
  width = int(claim[by+1:])

  claim_list.append((claim_number, left_border, top_border, length, width))

  for y in range(top_border, top_border+width):
    for x in range(left_border, left_border+length):
      fabric[x + 1000*y] += 1

for claim_number, left_border, top_border, length, width in claim_list:
  global unclaimed_list
  unclaimed = True
  unclaimed_list.add(claim_number)
  for y in range(top_border, top_border+width):
    for x in range(left_border, left_border+length):
      if unclaimed and fabric[x + 1000*y] >= 2 :
        unclaimed_list.remove(claim_number)
        unclaimed = False



print (unclaimed_list)