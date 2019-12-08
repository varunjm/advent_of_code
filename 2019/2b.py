import sys
from IntcodeComputer import IntcodeComputer

f = open(sys.argv[1], "r")
program = [int(element) for element in f.read().split(",")]
for noun in range(0, 99):
	for verb in range(0, 99):
		program[1] = noun
		program[2] = verb
		computer = IntcodeComputer(program[:])
		computer.run()
		if computer.fetch_mem(0) == 19690720:
			print (noun*100 + verb)
			sys.exit()
