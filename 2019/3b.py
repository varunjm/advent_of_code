import sys

dist_to_points = dict()
curr = (0, 0)
points = [(0,0)]
min_steps = 9223372036854775807
delta = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
steps2 = 0

def UpdatePoints(move):
  global curr
  global points
  move_vector = delta[move[0]]
  dist = int(move[1:])
  points.extend([(curr[0]+(move_vector[0]*i), curr[1]+(move_vector[1]*i)) for i in range(1, dist+1)])
  curr = points[-1]

# Identify intersections and find smallest number of steps needed to reach an intersection
def IdentifyIntersections(move):
  global curr
  global dist_to_points
  global steps2
  global min_steps

  move_vector = delta[move[0]]
  dist = int(move[1:])
  for i in range(1, dist+1):
    xy = (curr[0]+(move_vector[0]*i), curr[1]+(move_vector[1]*i))
    if xy in dist_to_points:
      min_steps = min(min_steps, dist_to_points[xy] + steps2 + i)
  curr = xy
  steps2 = steps2 + dist

f = open(sys.argv[1], "r")

#wire 1
map(UpdatePoints, f.readline().split(","))

for idx, point in enumerate(points):
  if point not in dist_to_points:
    dist_to_points[point] = idx

del dist_to_points[(0,0)]
curr = (0, 0)

#wire 2
map(IdentifyIntersections, f.readline().split(","))

print(min_steps)
