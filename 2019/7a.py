import sys
import itertools
from IntcodeComputer import IntcodeComputer
f = open(sys.argv[1], "r")

program = [int(element) for element in f.readline().split(",")]

max_thrust = -1
max_thrust_phases = None
for phases in itertools.permutations([0,1,2,3,4]):
  Amplifier = [IntcodeComputer(program[:]) for c in range(0,5)]
  output_signal = 0
  for idx, phase in enumerate(phases):
    Amplifier[idx].set_signal(output_signal)
    Amplifier[idx].set_phase(phase)
    output_signal = Amplifier[idx].run()
  if max_thrust < output_signal:
    max_thrust = output_signal
    max_thrust_phases = phases

print(max_thrust_phases)
print(max_thrust)