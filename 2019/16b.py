import sys

f = open(sys.argv[1], 'r')

sequence = f.read()
offset=int(sequence[0:7])
sequence = [int(c) for c in sequence.strip()]

temp = []
for i in range(0, 10000):
  temp.extend(sequence)
sequence = temp
total_size = len(sequence)

for phase in range(0, 100):
  for position in range(total_size-2, offset-1, -1):
    sequence[position] = abs(sequence[position] + sequence[position+1])%10

print (sequence[offset:offset+8])