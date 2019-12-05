import sys

f = open(sys.argv[1], "r")

total = sum([int(change) for change in f.readlines()])
print(total)

