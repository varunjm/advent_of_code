import sys

f = open(sys.argv[1], "r")

digits_count = dict()

layer_size = 25 * 6
min_zeros = layer_size
min_zero_layer = None
layer = 0
zeros = 0
ones = 0
twos = 0
pixel_counter = 0
for pixel in f.read():
  pixel_counter += 1
  zeros += 1 if pixel == '0' else 0
  ones += 1 if pixel == '1' else 0
  twos += 1 if pixel == '2' else 0
  
  # New layer
  if pixel_counter == layer_size:
    digits_count[layer] = (zeros, ones, twos)
    min_zeros, min_zero_layer = (zeros, layer) if zeros < min_zeros else (min_zeros, min_zero_layer)
    layer += 1
    zeros = 0
    ones = 0
    twos = 0
    pixel_counter = 0

print (digits_count[min_zero_layer])