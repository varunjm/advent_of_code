import sys
from IntcodeComputer import IntcodeComputer

f = open(sys.argv[1], 'r')

computer = IntcodeComputer([int(element) for element in f.read().split(",")], stop_at_print=True, DEBUG=False)
space_map = dict()
x = 0
y = 0
sum_alignment = 0
code = computer.run()
while code != None:
  print chr(code),
  if code == 10:
    y += 1
    max_x = x
    x = 0
  else:
    space_map[(x, y)] = code
    if code == 35 and y > 1 and x > 0 and x < max_x:
      if space_map[(x,y-1)] == 35 and space_map[(x,y-2)] == 35 and space_map[(x-1,y-1)] ==35 and space_map[(x+1,y-1)] == 35:
        sum_alignment += (x*(y-1)) 
    x += 1
  code = computer.run()
max_y = y

print (sum_alignment)
