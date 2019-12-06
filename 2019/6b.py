import sys
from collections import deque

f = open(sys.argv[1], "r")
orbital_graph = dict()

for orbit in f.readlines():
  brace = orbit.find(')')
  orbitee = orbit[:brace]
  orbiter = orbit[brace+1:-1]
  if orbiter == 'SAN':
    target = orbitee
  if orbiter == 'YOU':
    source = orbitee 
  if orbiter not in orbital_graph:
    orbital_graph[orbiter] = []
  if orbitee not in orbital_graph:
    orbital_graph[orbitee] = []
  orbital_graph[orbitee].append(orbiter)
  orbital_graph[orbiter].append(orbitee)

# print(orbital_graph)
print(target)

visited = set()
q = deque() 
q.append((source, 0))

while True:
  current, depth = q.popleft()
  if current == target:
    break
  if current not in visited:
    print (current, depth)
    visited.add(current)
    # print (current)
    # map(q.append, orbital_graph[current])
    for orbital in orbital_graph[current]:
      q.append((orbital, depth+1))

print (current, depth)