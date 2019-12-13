import sys
from os import system
from IntcodeComputer import IntcodeComputer
f = open(sys.argv[1], "r")
computer = IntcodeComputer([int(element) for element in f.read().split(",")], stop_at_print=True, DEBUG=False)
game_map = dict()

count = 0
max_x = 0
max_y = 0
while True:
  x = computer.run()
  if x == None:
    break
  max_x = x if x > max_x else max_x
  y = computer.run()
  tile_id = computer.run()
  max_y = x if y > max_y else max_y
  game_map[(x,y)] = tile_id
  count += 1 if tile_id == 2 else 0

print(count)