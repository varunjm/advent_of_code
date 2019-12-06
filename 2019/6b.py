import sys
from collections import deque

orbital_graph = dict()

# Build graph of orbitals
with open(sys.argv[1], "r") as orbits:
  for orbit in orbits:
    orbitee, orbiter = orbit.strip().split(')')
    if orbiter == 'SAN':
      target = orbitee 
    if orbiter == 'YOU':
      source = orbitee 
    orbital_graph[orbiter] = [] if orbiter not in orbital_graph else orbital_graph[orbiter]
    orbital_graph[orbitee] = [] if orbitee not in orbital_graph else orbital_graph[orbitee]
    orbital_graph[orbitee].append(orbiter)
    orbital_graph[orbiter].append(orbitee)

# Breadth first search
visited = set()
q = deque() 
q.append((source, 0))

while True:
  current, depth = q.popleft()
  if current == target:
    break
  if current not in visited:
    visited.add(current)
    for orbital in orbital_graph[current]:
      q.append((orbital, depth+1))

print (current, depth)