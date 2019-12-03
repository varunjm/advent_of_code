import sys

curr = (0, 0)
points = ["0,0"]
min_steps = 9223372036854775807
steps2 = 0

def UpdatePoints(move):
  global curr
  global points
  dist = int(move[1:])
  if move[0] == 'R':
    points.extend([ (str(curr[0]+i)+","+str(curr[1])) for i in range(1, dist+1)])
    curr = (curr[0]+dist, curr[1])
  elif move[0] == 'L':
    points.extend([ (str(curr[0]-i)+","+str(curr[1])) for i in range(1, dist+1)])
    curr = (curr[0]-dist, curr[1])
  elif move[0] == 'U':
    points.extend([ (str(curr[0])+","+str(curr[1]+i)) for i in range(1, dist+1)])
    curr = (curr[0], curr[1]+dist)
  elif move[0] == 'D':
    points.extend([ (str(curr[0])+","+str(curr[1]-i)) for i in range(1, dist+1)])
    curr = (curr[0], curr[1]-dist)

def IdentifyIntersections(move):
  global curr
  global points
  global steps2
  global min_steps

  dist = int(move[1:])
  if move[0] == 'R':
    for i in range(1, dist+1):
      xy = (str(curr[0]+i)+","+str(curr[1]))
      if xy in points:
        # print "Meeting at " + xy
        steps1 = points.index(xy) + 1
        min_steps = min(min_steps, steps1 + steps2 + i)
    curr = (curr[0]+dist, curr[1])
  elif move[0] == 'L':
    for i in range(1, dist+1):
      xy = (str(curr[0]-i)+","+str(curr[1]))
      if xy in points:
        # print "Meeting at " + xy
        steps1 = points.index(xy) + 1
        min_steps = min(min_steps, steps1 + steps2 + i)
    curr = (curr[0]-dist, curr[1])
  elif move[0] == 'U':
    for i in range(1, dist+1):
      xy = (str(curr[0])+","+str(curr[1]+i))
      if xy in points:
        # print "Meeting at " + xy
        steps1 = points.index(xy) + 1
        min_steps = min(min_steps, steps1 + steps2 + i)
    curr = (curr[0], curr[1]+dist)
  elif move[0] == 'D':
    for i in range(1, dist+1):
      xy = (str(curr[0])+","+str(curr[1]-i))
      if xy in points:
        # print "Meeting at " + xy
        steps1 = points.index(xy) + 1
        min_steps = min(min_steps, steps1 + steps2 + i)
    curr = (curr[0], curr[1]-dist)
  steps2 = steps2 + dist

f = open(sys.argv[1], "r")
wires = f.readlines()

for move in wires[0].split(","):
  UpdatePoints(move)

used = set()
points = [x for x in points if x not in used and (used.add(x) or True)]
points.remove("0,0")
curr = (0, 0)

# print(points)
for move in wires[1].split(","):
  IdentifyIntersections(move)

print(min_steps)
