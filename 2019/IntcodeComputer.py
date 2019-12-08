class IntcodeComputer:
  three_opnds_instr_codes = [1, 2, 7 ,8]
  two_opnds_instr_codes = [5, 6]
  operations = {
    1: lambda p1, p2: p1 + p2,
    2: lambda p1, p2: p1 * p2,
    5: lambda p1, p2, pc: p2 if p1 != 0 else pc + 3,
    6: lambda p1, p2, pc: p2 if p1 == 0 else pc + 3,
    7: lambda p1, p2: 1 if p1 < p2 else 0,
    8: lambda p1, p2: 1 if p1 == p2 else 0,
  }

  def __init__(self, instrs):
    self.instrs = instrs
    self.PC = 0
    self.phase = None
    self.signal = 0
  
  def set_phase(self, ph):
    self.phase = ph

  def set_signal(self, input):
    self.signal = input

  def fetch_1_opnd(self):
    param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(2, '0')
    param1 = self.instrs[self.PC+1] if param_mode[0] == '1' else self.instrs[self.instrs[self.PC+1]]
    return param1

  def fetch_2_opnds(self):
    param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(2, '0')
    param1 = self.instrs[self.PC+1] if param_mode[0] == '1' else self.instrs[self.instrs[self.PC+1]]
    param2 = self.instrs[self.PC+2] if param_mode[1] == '1' else self.instrs[self.instrs[self.PC+2]]
    return param1, param2

  def fetch_3_opnds(self):
    param1, param2 = self.fetch_2_opnds()
    dest = self.instrs[self.PC+3]
    return param1, param2, dest

  def exec_next_instr(self):
    opcode = self.instrs[self.PC]%100
    if opcode in self.three_opnds_instr_codes:
      param1, param2, dest = self.fetch_3_opnds()
      self.instrs[dest] = self.operations[opcode](param1, param2)
      self.PC += 4

    elif opcode == 3:
      self.instrs[self.instrs[self.PC+1]] = self.phase if self.phase != None else self.signal
      self.phase = None
      self.PC += 2

    elif opcode == 4:
      return_value = self.fetch_1_opnd()
      self.PC += 2
      return (opcode, return_value)

    elif opcode in self.two_opnds_instr_codes:
      param1, param2 = self.fetch_2_opnds()
      self.PC = self.operations[opcode](param1, param2, self.PC)

    elif opcode == 99:
      return (opcode, None)

    return (opcode, None)

  def run(self):
    result = None
    opcode = -1
    while not result and opcode != 99:
      opcode, result = self.exec_next_instr()
    return result

  def print_program(self):
    print (self.instrs)
  
  def fetch_mem(self, loc):
    return self.instrs[loc]
