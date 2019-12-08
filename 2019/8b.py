import sys

f = open(sys.argv[1], "r")

layer_size = 25 * 6
Image = [-1 for y in range(layer_size)] 
idx = 0
for pixel in f.read():
  if Image[idx%layer_size] == -1:
    if pixel == '0':
      Image[idx%layer_size] = 0
    elif pixel == '1':
      Image[idx%layer_size] = 1
  idx += 1

# Display image
for idx, pixel in enumerate(Image):
  if idx % 25 == 0:
    print('')
  print pixel,
print('')
