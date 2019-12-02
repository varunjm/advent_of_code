import sys

f = open(sys.argv[1], "r")

orig_array = [int(element) for element in f.read().split(",")]

noun = 12
verb = 2

array = orig_array[:]
index = 0
array[1] = noun
array[2] = verb

while array[index] != 99:
	if array[index] == 1:
		array[array[index+3]] = array[array[index+1]] + array[array[index+2]]
	elif array[index] == 2 :
		array[array[index+3]] = array[array[index+1]] * array[array[index+2]]
	else:
		print ("ERROR")
		sys.exit()

	index = index + 4

print (array[0])

