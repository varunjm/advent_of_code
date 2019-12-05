import sys

f = open(sys.argv[1], "r")

array = [int(element) for element in f.read().split(",")]


index = 0
input_value = 1

while array[index]%100 != 99:
  opcode = array[index]%100
  param_mode = str(array[index]/100)[::-1].ljust(2, '0')

  if opcode == 1 or opcode == 2:
    param1 = array[index+1] if param_mode[0] == '1' else array[array[index+1]]
    param2 = array[index+2] if param_mode[1] == '1' else array[array[index+2]]
    if opcode == 1:
      array[array[index+3]] = param1 + param2
      index = index + 4
    elif opcode == 2:
      array[array[index+3]] = param1 * param2
      index = index + 4
  
  elif opcode == 3:
    array[array[index+1]] = input_value
    index = index + 2
  elif opcode == 4:
    print(array[array[index+1]])
    index = index + 2
  else:
    print ("ERROR")
    sys.exit()

print array
