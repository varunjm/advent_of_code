import sys

f = open(sys.argv[1], 'r')
space = []
asteroid_lines = dict()
asteroids_on_line = dict()

def calc_line(asteroid1, asteroid2):
  m = float('inf') if (asteroid1[0] == asteroid2[0]) else (asteroid1[1]-asteroid2[1]) / (asteroid1[0]-asteroid2[0])
  c = asteroid1[0] if (asteroid1[0] == asteroid2[0]) else (asteroid1[1] - m * asteroid1[0])
  m = 0 if m == -0 else m
  c = 0 if c == -0 else c
  return (float('{:0.3e}'.format(m)), float('{:0.3e}'.format(c)))

def is_line_end_point(asteroids, asteroid):
  x_high = True
  y_high = True
  x_low = True
  y_low = True
  for value in asteroids:
    if value[0] < asteroid[0]:
      x_low = False
    elif value[0] > asteroid[0]:
      x_high = False
    if value[1] < asteroid[1]:
      y_low = False
    elif value[1] > asteroid[1]:
      y_high = False
  return (x_low != x_high or y_low != y_high)

def find_nearest_on_line(station, line, direction):
  min_dist = 1000
  closest_asteroid = None
  correct_side = {
    'east': lambda x1, x2: x1 >= x2,
    'west': lambda x1, x2: x1 <= x2
  }
  for asteroid in asteroids_on_line[line]:
    dist = abs(asteroid[0]-station[0])+abs(asteroid[1]-station[1])
    if (asteroid != station and dist < min_dist and correct_side[direction](asteroid[0],station[0])):
        min_dist = dist
        closest_asteroid = asteroid

  if closest_asteroid == None:
    return False
  asteroids_on_line[line].remove(closest_asteroid)
  return closest_asteroid

def laser_sweep_side (destroyed_count, direction):
  latest_asteroid = False
  for line in sorted_lines:
    latest_asteroid = find_nearest_on_line(station, line, direction)
    if latest_asteroid != False:
      destroyed_count += 1
      if destroyed_count == 200:
        return (latest_asteroid, destroyed_count)
  return (latest_asteroid, destroyed_count)

# list of asteroids
for y, line in enumerate(f.readlines()):
  for x, point in enumerate(line):
    if point == '#':
      xy = (float(x),float(y))
      space.append(xy)
      asteroid_lines[xy] = set()

#map and reverse map all asteroids to lines
for asteroid1 in space:
  for asteroid2 in space:
    if asteroid1 != asteroid2:
      m, c = calc_line (asteroid1, asteroid2)
      asteroids_on_line[(m,c)] = set() if (m,c) not in asteroids_on_line else asteroids_on_line[(m,c)]
      asteroids_on_line[(m,c)].add(asteroid1)
      asteroids_on_line[(m,c)].add(asteroid2)
      asteroid_lines[asteroid1].add((m,c))
      asteroid_lines[asteroid2].add((m,c))

#count visibility for each asteroid
max_visibility = -1
for asteroid in space:
  count = 0
  for line in asteroid_lines[asteroid]:
    count += 1 if is_line_end_point(asteroids_on_line[line], asteroid) else 2
  station, max_visibility = (asteroid, count) if max_visibility < count else (station, max_visibility)

print ('station', station)
print ('# of asteroids visible', max_visibility)

# sort lines by slope (which is the first field of a line tuple)
sorted_lines = sorted(asteroid_lines[station])
#move vertical line (slope = inf) from end of list to front of list
sorted_lines = [sorted_lines[-1]] + sorted_lines[:-1]

destroyed_count = 0
direction = 'east'
while destroyed_count != 200:
  latest_asteroid, destroyed_count = laser_sweep_side(destroyed_count, direction)
  direction = 'east' if direction == 'west' else 'west'

print('200th asteroid', latest_asteroid)
