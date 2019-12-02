def fuel_weight(fuel):
	if fuel < 7:
		return fuel 
	additional = fuel_weight(fuel/3-2)
	return fuel + additional

f = open("./input/1.in", "r")
weights = f.readlines()
fuel=0

for weight in weights:
	fuel = fuel + fuel_weight(int(weight)/3-2)

print(fuel)


