import sys
import itertools

f = open(sys.argv[1], "r")

class IntcodeComputer:
  four_op_instr_codes = [1, 2, 7 ,8]
  two_op_instr_codes = [5, 6]

  def __init__(self, instrs):
    #list of instructions
    self.instrs = instrs
    #program counter
    self.PC = 0
    self.phase = None
    self.signal = None
  
  def set_phase(self, ph):
    self.phase = ph

  def set_signal(self, input):
    self.signal = input

  def print_computer (self):
    print ('instr', self.instrs)
    print ('PC', self.PC)
    print ('Signal', self.signal)
    print ('Phase', self.phase)

  def fetch_2_params(self):
    param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(2, '0')
    param1 = self.instrs[self.PC+1] if param_mode[0] == '1' else self.instrs[self.instrs[self.PC+1]]
    param2 = self.instrs[self.PC+2] if param_mode[1] == '1' else self.instrs[self.instrs[self.PC+2]]
    return param1, param2

  def fetch_1_param(self):
    param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(2, '0')
    param1 = self.instrs[self.PC+1] if param_mode[0] == '1' else self.instrs[self.instrs[self.PC+1]]
    return param1

  def exec_next_instr(self):
    opcode = self.instrs[self.PC]%100
    if opcode in self.four_op_instr_codes:
      param1, param2 = self.fetch_2_params()
      if opcode == 1:
        self.instrs[self.instrs[self.PC+3]] = param1 + param2
      elif opcode == 2:
        self.instrs[self.instrs[self.PC+3]] = param1 * param2
      elif opcode == 7:
        self.instrs[self.instrs[self.PC+3]] = 1 if param1 < param2 else 0
      elif opcode == 8:
        self.instrs[self.instrs[self.PC+3]] = 1 if param1 == param2 else 0
      self.PC += 4
    elif opcode == 3:
      if self.phase != None:
        self.instrs[self.instrs[self.PC+1]] = self.phase
        self.phase = None
      else :
        self.instrs[self.instrs[self.PC+1]] = self.signal
      self.PC += 2
    elif opcode == 4:
      return_value = self.fetch_1_param()
      self.PC += 2
      return return_value
    elif opcode in self.two_op_instr_codes:
      param1, param2 = self.fetch_2_params()
      if (param1 != 0 and opcode == 5) or (param1 == 0 and opcode == 6) :
        self.PC = param2
      else:
        self.PC += 3
    elif opcode == 99:
      return True
    else:
      print ("ERROR")
      sys.exit()
    return False
  
  def run(self):
    result = None
    while not result:
      result = self.exec_next_instr()
    return result

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