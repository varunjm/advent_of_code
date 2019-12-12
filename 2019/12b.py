import sys
from fractions import gcd

f = open(sys.argv[1], 'r')
moons = dict()
moons2 = dict()
velocities = dict()
velocities2 = dict()
periods = {
  0: None,
  1: None,
  2: None,
}

def update_positions():
  global moons
  global velocities

  for idx, moon in enumerate(moons.values()):
    moons[idx] = [moon[0] + velocities[idx][0], moon[1] + velocities[idx][1], moon[2] + velocities[idx][2]]

def update_velocities():
  global moons
  global velocities
  for idx1, moon1 in enumerate(moons.values()):
    for moon2 in moons.values():
      velocity = [0,0,0]
      for axis in [0, 1, 2]:
        if moon1[axis] < moon2[axis]:
          velocity[axis] = velocities[idx1][axis] + 1
        elif moon1[axis] == moon2[axis]:
          velocity[axis] = velocities[idx1][axis]
        else:
          velocity[axis] = velocities[idx1][axis] - 1
      velocities[idx1] = velocity

def calc_axes_periods(time):
  global moons
  global moons2
  global velocities
  global velocities2
  global periods

  for axis in [0, 1, 2]:
    match_count = 0
    for idx, moon in enumerate(moons.values()):
      if periods[axis] == None and moon[axis] == moons2[idx][axis] and velocities[idx][axis] == velocities2[idx][axis]:
        match_count += 1
    periods[axis] = time if periods[axis] == None and match_count == len(moons) else periods[axis]

  return periods[0] != None and periods[1] != None and periods[2] != None 

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

for idx, line in enumerate(f.readlines()):
  moon = line.strip().split(',')
  moon = [int(moon[0][3:]), int(moon[1][3:]), int(moon[2][3:-1])]
  moons[idx] = moon
  moons2[idx] = moon
  velocities[idx] = [0, 0, 0]
  velocities2[idx] = [0, 0, 0]

first = True
time = 0
while True:
  update_positions()
  if not first and calc_axes_periods(time):
    break
  first = False
  time += 1
  update_velocities()

print (lcm(lcm(periods[0], periods[1]), periods[2]))