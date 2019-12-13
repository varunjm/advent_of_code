import sys
from IntcodeComputer import IntcodeComputer
from os import system
import time

f = open(sys.argv[1], "r")
game_map = dict()

def next_input():
  global game_map
  global ball
  global paddle
  # for y in range(0, 25):
  #   for x in range(0, 42):
  #     if (x, y) in game_map and game_map[(x, y)] != 0:
  #       print (game_map[(x, y)], end='')
  #     else:
  #       print (' ', end='')
  #   print ('')
  # print("_________________________________________________________________________________")
  code_input_val = -1 if paddle > ball else 1 if paddle < ball else 0
  return code_input_val

computer = IntcodeComputer([int(element) for element in f.read().split(",")], stop_at_print=True, DEBUG=False, input_func=next_input)
computer.set_mem(0, 2)
ball = -1
paddle = -1
while True:
  x = computer.run()
  if x == None:
    break
  y = computer.run()
  tile_id = computer.run()
  if x == -1 and y == 0:
    print ('Score', tile_id)
  ball = x if tile_id == 4 else ball
  paddle = x if tile_id == 3 else paddle
  game_map[(x,y)] = tile_id
