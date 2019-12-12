import sys

f = open(sys.argv[1], 'r')
moons = []
velocities = []

def update_positions():
  global moons
  global velocities
  for idx, moon in enumerate(moons):
    moons[idx] = [moon[0] + velocities[idx][0], moon[1] + velocities[idx][1], moon[2] + velocities[idx][2]]

def update_velocities():
  global moons
  global velocities
  for idx1, moon1 in enumerate(moons):
    for moon2 in moons:
      for axis in [0, 1, 2]:
        velocities[idx1][axis] += 1 if moon1[axis] < moon2[axis] else 0 if moon1[axis] == moon2[axis] else -1

def total_energy():
  global moons
  global velocities

  energy = 0
  for idx, moon in enumerate(moons):
    energy += sum([abs(i) for i in moon]) * sum([abs(i) for i in velocities[idx]])

  return energy

for line in f.readlines():
  moon = line.strip().split(',')
  moon = [int(moon[0][3:]), int(moon[1][3:]), int(moon[2][3:-1])]
  moons.append(moon)
  velocities.append([0, 0, 0])

end_of_time = 1000
# print(moons)
for time in range(0, end_of_time):
  update_positions()
  update_velocities()
  # print moons, velocities

update_positions()
print moons, velocities

print (total_energy())