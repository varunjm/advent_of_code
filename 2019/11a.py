import sys
from IntcodeComputer import IntcodeComputer

f = open(sys.argv[1], "r")
computer = IntcodeComputer([int(element) for element in f.read().split(",")], stop_at_print=True, DEBUG=False)
panels = dict()
computer.set_phase(None)

new_xy_dir = {
  ('up', 0):   lambda xy, current_dir, new_dir: ((xy[0]-1, xy[1]), 'left'),
  ('down', 1): lambda xy, current_dir, new_dir: ((xy[0]-1, xy[1]), 'left'),
  ('up', 1):   lambda xy, current_dir, new_dir: ((xy[0]+1, xy[1]), 'right'),
  ('down', 0): lambda xy, current_dir, new_dir: ((xy[0]+1, xy[1]), 'right'),
  ('left', 0): lambda xy, current_dir, new_dir: ((xy[0], xy[1]+1), 'down'),
  ('right', 1): lambda xy, current_dir, new_dir: ((xy[0], xy[1]+1), 'down'),
  ('left', 1): lambda xy, current_dir, new_dir: ((xy[0], xy[1]-1), 'up'),
  ('right', 0): lambda xy, current_dir, new_dir: ((xy[0], xy[1]-1), 'up'),
}

xy = (0, 0)
current_dir = 'up'
color = 0

min_x = 0
min_y = 0
max_x = 0
max_y = 0

while True:
  computer.set_signal(color)
  new_color = computer.run()
  if new_color == None:
    break
  new_dir = computer.run()
  panels[xy] = new_color
  xy, current_dir = new_xy_dir[(current_dir, new_dir)](xy, current_dir, new_dir)
  color = panels[xy] if xy in panels else 0

print (len(panels))

