import sys

f = open(sys.argv[1], 'r')
base_pattern = [0, 1, 0, -1]
sequence = f.read()
sequence = [int(c) for c in sequence.strip()]
total_size = len(sequence)
sequence = [sequence, sequence]
curr = 0
for phase in range(0, 100):
  for position in range(1, total_size+1):
    value = sum([sequence[curr][idx] * base_pattern[((idx+1)/position)%4] for idx in range(0, total_size)])
    sequence[(curr+1)%2][position-1] = (abs(value) % 10)
    curr = (curr+1)%2
print (sequence[curr][0:8])