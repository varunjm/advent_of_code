import sys
from IntcodeComputer import IntcodeComputer
import copy

f = open(sys.argv[1], 'r')

Intcode = [int(element) for element in f.read().split(",")]
# computer = IntcodeComputer(Intcode[:], stop_at_print=True, DEBUG=True)

space_map = dict()
dust = 0
count = 0
for y in range(0, 50):
  for x in range(0, 50):
    comp = IntcodeComputer(Intcode[:], stop_at_print=True, DEBUG=False)
    comp.set_phase(x)
    comp.set_signal(y)
    code = comp.run()
    count += int(code)
    print code, 
  print ''

print (count)