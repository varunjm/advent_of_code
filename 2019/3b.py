import sys

dist_to_points = dict()
curr = (0, 0)
points = [(0,0)]
min_steps = 9223372036854775807
steps2 = 0

def getstr(xy):
  return (str(xy[0])+","+str(xy[1]))

def UpdatePoints(move):
  global curr
  global points
  dist = int(move[1:])
  if move[0] == 'R':
    points.extend([ (curr[0]+i, curr[1]) for i in range(1, dist+1)])
    curr = (curr[0]+dist, curr[1])
  elif move[0] == 'L':
    points.extend([ (curr[0]-i, curr[1]) for i in range(1, dist+1)])
    curr = (curr[0]-dist, curr[1])
  elif move[0] == 'U':
    points.extend([ (curr[0], curr[1]+i) for i in range(1, dist+1)])
    curr = (curr[0], curr[1]+dist)
  elif move[0] == 'D':
    points.extend([ (curr[0], curr[1]-i) for i in range(1, dist+1)])
    curr = (curr[0], curr[1]-dist)

def IdentifyIntersections(move):
  global curr
  global dist_to_points
  global steps2
  global min_steps

  dist = int(move[1:])
  if move[0] == 'R':
    for i in range(1, dist+1):
      xy = getstr((curr[0]+i, curr[1]))
      if xy in dist_to_points:
        # print "Meeting at " + xy
        min_steps = min(min_steps, dist_to_points[xy] + steps2 + i)
    curr = (curr[0]+dist, curr[1])
  elif move[0] == 'L':
    for i in range(1, dist+1):
      xy = getstr((curr[0]-i, curr[1]))
      if xy in dist_to_points:
        # print "Meeting at " + xy
        min_steps = min(min_steps, dist_to_points[xy] + steps2 + i)
    curr = (curr[0]-dist, curr[1])
  elif move[0] == 'U':
    for i in range(1, dist+1):
      xy = getstr((curr[0], curr[1]+i))
      if xy in dist_to_points:
        # print "Meeting at " + xy
        min_steps = min(min_steps, dist_to_points[xy] + steps2 + i)
    curr = (curr[0], curr[1]+dist)
  elif move[0] == 'D':
    for i in range(1, dist+1):
      xy = getstr((curr[0], curr[1]-i))
      if xy in dist_to_points:
        # print "Meeting at " + xy
        min_steps = min(min_steps, dist_to_points[xy] + steps2 + i)
    curr = (curr[0], curr[1]-dist)
  steps2 = steps2 + dist

f = open(sys.argv[1], "r")

#wire 1
for move in f.readline().split(","):
  UpdatePoints(move)

used = set()
# points = [x for x in points if x not in used and (used.add(x) or True)]
for idx, point in enumerate(points):
  if point not in used:
    used.add(point)
    xy = getstr(point)
    dist_to_points[xy] = idx

del dist_to_points["0,0"]
curr = (0, 0)

# print(points)

#wire 2
for move in f.readline().split(","):
  IdentifyIntersections(move)

print(min_steps)
