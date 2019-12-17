import sys
from IntcodeComputer import IntcodeComputer

f = open(sys.argv[1], 'r')

input_list = ['A',',','C',',','A',',','B',',','C',',','B',',','A',',','B',',','C',',','B','\n','L',',','8',',','R',',','1','0',',','L',',','1','0','\n','L',',','4',',','L',',','6',',','L',',','8',',','L',',','8','\n','R',',','1','0',',','L',',','8',',','L',',','8',',','L',',','1','0','\n','n','\n']
counter = 0

def next_input():
  global input_list
  global counter
  val = input_list[counter]
  counter += 1
  return ord(val)

computer = IntcodeComputer([int(element) for element in f.read().split(",")], stop_at_print=True, DEBUG=False, input_func=next_input)
computer.set_mem(0, 2)

space_map = dict()
# intersections = set()
x = 0
y = 0
dust = 0
code = computer.run()
while code != None:
  if counter == len(input_list):
    if code > 128:
      print ('dust', code)
      break
  else:
    print chr(code),
    if code == 10:
      y += 1
      max_x = x
      x = 0
    else:
      space_map[(x, y)] = code
      x += 1
  code = computer.run()
max_y = y
