import sys

f = open(sys.argv[1], "r")

orbit_map = dict()
orbit_count = dict()

for orbit in f.readlines():
  brace = orbit.find(')')
  orbitee = orbit[:brace]
  orbiter = orbit[brace+1:-1]
  if orbiter not in orbit_map:
    orbit_map[orbiter] = orbitee
    # print orbit_map
  # else:
  #   orbit_map[orbiter] = orbit_map[orbiter].extend(orbitee)
  # print(orbitee, orbiter)

for orbiter in orbit_map.keys():
  orbitee = orbit_map[orbiter]
  count = 0
  while orbitee:
    count += 1
    orbitee = orbit_map[orbitee] if orbitee in orbit_map.keys() else False
  orbit_count[orbiter] = count

# print(orbit_map)
# print(orbit_count)
print(sum(orbit_count.values()))