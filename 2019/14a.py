import sys

f = open(sys.argv[1], 'r')

def calculate_preference(chemical):
  if chemical not in reaction_preference:
    reaction_preference[chemical] = 0
    for input_req in chemical_reactions[chemical]:
      reaction_preference[chemical] = max(calculate_preference(input_req[0]) + 1, reaction_preference[chemical])

  return reaction_preference[chemical]

chemical_reactions = dict()
# minimun quanta of generating each chemical
chemical_min = dict()
# keep track of all raw materials other than ORE
raw_materials = dict()
reaction_preference = {'ORE':0}

for reaction in f.readlines():
  io = reaction.strip().split("=>")
  input_chemicals = io[0].strip().split(',')
  output_chemical = io[1].strip().split(' ')
  chemical_reactions[output_chemical[1]] = [(chemical.strip().split(' ')[1], int(chemical.strip().split(' ')[0])) for chemical in input_chemicals]
  chemical_min[output_chemical[1]] = int(output_chemical[0])

calculate_preference('FUEL')
ore_needed = 0
#require 1 FUEL
raw_materials['FUEL'] = 1

while len(raw_materials) != 0:
  req = max([(reaction_preference[key], key) for key in raw_materials.keys()])[1]
  how_much = raw_materials[req]
  del raw_materials[req]
  for chemical in chemical_reactions[req]:
    multiple = how_much / chemical_min[req] + (1 if how_much % chemical_min[req] else 0)
    if chemical[0] == 'ORE':
      ore_needed += chemical[1] * multiple
    else:
      if chemical[0] not in raw_materials:
        raw_materials[chemical[0]] = 0  
      raw_materials[chemical[0]] += chemical[1] * multiple

print (ore_needed)
print (1000000000000/ore_needed)