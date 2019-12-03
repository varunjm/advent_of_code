import sys

curr = (0, 0)
points = {(0,0)}
min_dist = 9223372036854775807

def UpdatePoints(move):
  global curr
  global points
  dist = int(move[1:])
  if move[0] == 'R':
    points.update([ ((curr[0]+i),(curr[1])) for i in range(1, dist+1)])
    curr = (curr[0]+dist, curr[1])
  elif move[0] == 'L':
    points.update([ ((curr[0]-i),(curr[1])) for i in range(1, dist+1)])
    curr = (curr[0]-dist, curr[1])
  elif move[0] == 'U':
    points.update([ ((curr[0]), (curr[1]+i)) for i in range(1, dist+1)])
    curr = (curr[0], curr[1]+dist)
  elif move[0] == 'D':
    points.update([ ((curr[0]), (curr[1]-i)) for i in range(1, dist+1)])
    curr = (curr[0], curr[1]-dist)

# Identify intersections and find the intersection nearest(manhattan distance) to origin
def IdentifyIntersections(move):
  global curr
  global points
  global min_dist

  dist = int(move[1:])
  if move[0] == 'R':
    for i in range(1, dist+1):
      xy = ((curr[0]+i),(curr[1]))
      if xy in points:
        min_dist = min(min_dist, abs(curr[0]+i) + abs(curr[1]))
    curr = (curr[0]+dist, curr[1])
  elif move[0] == 'L':
    for i in range(1, dist+1):
      xy = ((curr[0]-i),(curr[1]))
      if xy in points:
        min_dist = min(min_dist, abs(curr[0]-i) + abs(curr[1]))
    curr = (curr[0]-dist, curr[1])
  elif move[0] == 'U':
    for i in range(1, dist+1):
      xy = ((curr[0]),(curr[1]+i))
      if xy in points:
        min_dist = min(min_dist, abs(curr[0]) + abs(curr[1]+i))
    curr = (curr[0], curr[1]+dist)
  elif move[0] == 'D':
    for i in range(1, dist+1):
      xy = ((curr[0]),(curr[1]-i))
      if xy in points:
        min_dist = min(min_dist, abs(curr[0]) + abs(curr[1]-i))
    curr = (curr[0], curr[1]-dist)

f = open(sys.argv[1], "r")

#wire 1
for move in f.readline().split(","):
  UpdatePoints(move)

points.remove((0,0))
curr = (0, 0)

#wire 2
for move in f.readline().split(","):
  IdentifyIntersections(move)

print(min_dist)
