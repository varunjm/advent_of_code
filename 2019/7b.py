import sys
import itertools
from IntcodeComputer import IntcodeComputer

f = open(sys.argv[1], "r")

program = [int(element) for element in f.readline().split(",")]

max_thrust = -1
max_thrust_phases = None
for phases in itertools.permutations([5,6,7,8,9]):
  Amplifier = [IntcodeComputer(program[:]) for c in range(0,5)]
  Amplifier[0].set_signal(0)
  for idx, phase in enumerate(phases):
    Amplifier[idx].set_phase(phase)

  idx = 0
  thrust = 0
  output_signal = 0
  while output_signal != None:
    thrust = output_signal
    output_signal = Amplifier[idx].run()
    idx = (idx + 1) % 5
    Amplifier[idx].set_signal(output_signal)

  max_thrust, max_thrust_phases = (thrust, phases) if max_thrust < thrust else (max_thrust, max_thrust_phases)

print(max_thrust_phases)
print(max_thrust)