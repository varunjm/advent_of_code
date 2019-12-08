import sys
from IntcodeComputer import IntcodeComputer

f = open(sys.argv[1], "r")
computer = IntcodeComputer([int(element) for element in f.read().split(",")])
computer.set_phase(None)
computer.set_signal(5)
print(computer.run())
