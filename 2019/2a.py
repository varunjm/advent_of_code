import sys
from IntcodeComputer import IntcodeComputer

f = open(sys.argv[1], "r")
program = [int(element) for element in f.read().split(",")]
program[1] = 12 #noun
program[2] = 2  #verb
computer = IntcodeComputer(program)
computer.run()
print(computer.fetch_mem(0))
