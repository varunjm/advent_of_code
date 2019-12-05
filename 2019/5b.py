import sys

f = open(sys.argv[1], "r")

array = [int(element) for element in f.readline().split(",")]


index = 0
input_value = int(sys.argv[2])

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
    array[array[index+1]] = input_value
    index += 2
  elif opcode == 4:
    param1 = array[index+1] if param_mode[0] == '1' else array[array[index+1]]
    print(param1)
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

# print array
