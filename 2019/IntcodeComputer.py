import types

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
    9: lambda p1, rel_base: p1 + rel_base,
  }

  def __init__(self, instrs, stop_at_print = True, input_func = None, DEBUG = False):
    self.instrs = instrs
    self.instrs.extend([0 for i in range(0, 5000)])
    self.PC = 0
    self.phase = None
    if input_func != None:
      self.signal = input_func
    self.relative_base = 0
    self.stop_at_print = stop_at_print
    self.DEBUG_MODE = DEBUG
  
  def set_phase(self, ph):
    self.phase = ph

  def set_signal(self, input):
    self.signal = input

  def param_value(self, param_mode, offset):
    if param_mode == '1':
      param = self.instrs[self.PC+offset]
    elif param_mode == '2':
      param = self.instrs[self.relative_base + self.instrs[self.PC+offset]]
    else:
      param = self.instrs[self.instrs[self.PC+offset]]
    return param

  def fetch_1_opnd(self):
    param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(3, '0')
    param1 = self.param_value(param_mode[0], 1)
    return param1

  def fetch_2_opnds(self):
    param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(3, '0')
    param1 = self.param_value(param_mode[0], 1)
    param2 = self.param_value(param_mode[1], 2)
    return param1, param2

  def fetch_3_opnds(self):
    param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(3, '0')
    param1 = self.param_value(param_mode[0], 1)
    param2 = self.param_value(param_mode[1], 2)
    dest = self.instrs[self.PC+3]
    if param_mode[2] == '2':
      dest += self.relative_base
    return param1, param2, dest

  def exec_next_instr(self):
    opcode = self.instrs[self.PC]%100
    if self.DEBUG_MODE:
      print (opcode)
    if opcode in self.three_opnds_instr_codes:
      param1, param2, dest = self.fetch_3_opnds()
      self.instrs[dest] = self.operations[opcode](param1, param2)
      self.PC += 4
      if self.DEBUG_MODE:
        print (param1, param2)

    elif opcode == 3:
      param_mode = str(self.instrs[self.PC]/100)[::-1].ljust(2, '0')
      input_value = self.signal() if isinstance(self.signal, types.FunctionType) else self.signal
      if param_mode[0] == '0':
        self.instrs[self.instrs[self.PC+1]] = self.phase if self.phase != None else input_value
      elif param_mode[0] == '2':
        self.instrs[self.relative_base+ self.instrs[self.PC+1]] = self.phase if self.phase != None else input_value
      if self.DEBUG_MODE:
        print ('input', input_value)
      self.phase = None
      self.PC += 2

    elif opcode == 4:
      return_value = self.fetch_1_opnd()
      self.PC += 2
      if self.stop_at_print:
        return (opcode, return_value)
      else :
        print (return_value)

    elif opcode in self.two_opnds_instr_codes:
      param1, param2 = self.fetch_2_opnds()
      self.PC = self.operations[opcode](param1, param2, self.PC)
      if self.DEBUG_MODE:
        print (param1, param2, 'PC = ', self.PC)

    elif opcode == 9:
      param1 = self.fetch_1_opnd()
      self.relative_base = self.operations[opcode](param1, self.relative_base)
      self.PC += 2
      if self.DEBUG_MODE:
        print (param1, 'relative_base = ', self.relative_base)

    elif opcode == 99:
      return (opcode, None)

    return (opcode, None)

  def run(self):
    result = None
    opcode = -1
    while result == None and opcode != 99:
      opcode, result = self.exec_next_instr()
    return result

  def print_program(self):
    print (self.instrs)

  def fetch_mem(self, loc):
    return self.instrs[loc]

  def set_mem(self, loc, value):
    self.instrs[loc] = value
