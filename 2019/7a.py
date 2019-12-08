import sys
import itertools

f = open(sys.argv[1], "r")

program = [int(element) for element in f.readline().split(",")]
thrust_map = dict()

def RunAmplifier (array, phase, input):
  if (phase, input) in thrust_map:
    return thrust_map[(phase, input)]
  index = 0
  return_value = None
  while array[index]%100 != 99:
    opcode = array[index]%100
    param_mode = str(array[index]/100)[::-1].ljust(2, '0')
    if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
      param1 = array[index+1] if param_mode[0] == '1' else array[array[index+1]]
      param2 = array[index+2] if param_mode[1] == '1' else array[array[index+2]]
      if opcode == 1:
        array[array[index+3]] = param1 + param2
      elif opcode == 2:
        array[array[index+3]] = param1 * param2
      elif opcode == 7:
        array[array[index+3]] = 1 if param1 < param2 else 0
      elif opcode == 8:
        array[array[index+3]] = 1 if param1 == param2 else 0
      index += 4
    elif opcode == 3:
      if phase != None:
        array[array[index+1]] = phase
        phase = None
      else :
        array[array[index+1]] = input
      index += 2
    elif opcode == 4:
      param1 = array[index+1] if param_mode[0] == '1' else array[array[index+1]]
      return_value = param1
      index += 2
    elif opcode == 5 or opcode == 6:
      param1 = array[index+1] if param_mode[0] == '1' else array[array[index+1]]
      param2 = array[index+2] if param_mode[1] == '1' else array[array[index+2]]
      if (param1 != 0 and opcode == 5) or (param1 == 0 and opcode == 6) :
        index = param2
      else:
        index += 3
    else:
      print ("ERROR")
      sys.exit()
  thrust_map[(phase, input)] = return_value
  return return_value

max_thrust = -1
max_thrust_phases = None
for phases in itertools.permutations([0,1,2,3,4]):
  output_signal = 0
  for phase in phases:
    output_signal = RunAmplifier (program[:], phase, output_signal)
  if max_thrust < output_signal:
    max_thrust = output_signal
    max_thrust_phases = phases

print(max_thrust_phases)
print(max_thrust)


