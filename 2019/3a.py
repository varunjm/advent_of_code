import sys

curr = (0, 0)
points = {(0,0)}
min_dist = 9223372036854775807
delta = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def manhattan_dist(xy):
  return abs(xy[0]) + abs(xy[1])

def UpdatePoints(move):
  global curr
  global points
  move_vector = delta[move[0]]
  dist = int(move[1:])
  points.update([(curr[0]+(move_vector[0]*i), curr[1]+(move_vector[1]*i)) for i in range(1, dist+1)])
  curr = (curr[0]+(move_vector[0]*dist), curr[1]+(move_vector[1]*dist))

# Identify intersections and find the intersection nearest(manhattan distance) to origin
def IdentifyIntersections(move):
  global curr
  global points
  global min_dist

  move_vector = delta[move[0]]
  dist = int(move[1:])
  for i in range(1, dist+1):
    xy = (curr[0]+(move_vector[0]*i), curr[1]+(move_vector[1]*i))
    if xy in points:
      min_dist = min(min_dist, manhattan_dist(xy))
  curr = xy

f = open(sys.argv[1], "r")

#wire 1
map(UpdatePoints, f.readline().split(","))

points.remove((0,0))
curr = (0, 0)

#wire 2
map(IdentifyIntersections, f.readline().split(","))

print(min_dist)
