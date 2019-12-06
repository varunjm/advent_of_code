import sys

orbit_map = dict()
orbit_count = dict()

with open(sys.argv[1], "r") as orbits:
  for orbit in orbits:
    orbitee, orbiter = orbit.strip().split(')')
    if orbiter not in orbit_map:
      orbit_map[orbiter] = orbitee

for orbiter in orbit_map:
  orbitee = orbit_map[orbiter]
  count = 0
  while orbitee:
    count, orbitee = (orbit_count[orbitee] + count + 1, None) if orbitee in orbit_count else (count + 1, orbit_map[orbitee]) if orbitee in orbit_map else (count + 1, None)
  orbit_count[orbiter] = count

print(sum(orbit_count.values()))