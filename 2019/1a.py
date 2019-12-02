import sys

f = open(sys.argv[1], "r")

weights = f.readlines()
fuel=0

for weight in weights:
	fuel = fuel + (int(weight)/3-2)

print(fuel)
