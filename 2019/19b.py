import sys
from IntcodeComputer import IntcodeComputer
import copy

f = open(sys.argv[1], 'r')

Intcode = [int(element) for element in f.read().split(",")]

space_map = dict()
ans = None

# First pick larger range but with bigger steps x -> (1500, 500, -10)
#                                               y -> (1500, 500, -10)
# Through trial and error get close to the answer then use smaller range and switch step size 1
for y in range(1150, 950, -1):
  for x in range(780, 650, -1):
    comp = IntcodeComputer(Intcode[:], stop_at_print=True, DEBUG=False)
    comp.set_phase(x)
    comp.set_signal(y)
    code = comp.run()
    space_map[(x,y)] = int(code)
    if (x+99, y+99) in space_map:
      if space_map[(x,y)] == 1 and space_map[(x+99,y)] == 1 and space_map[(x,y+99)] == 1 and space_map[(x+99,y+99)]:
        ans = (x, y)

print ans