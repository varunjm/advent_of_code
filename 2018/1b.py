import sys

f = open(sys.argv[1], "r")
change_list = [ int(change) for change in f.readlines() ]
freq_reached = set()

def  evaluate_all_changes(curr_freq):
  global freq_reached
  freq_found = False

  for change in change_list:
    curr_freq += change
    if curr_freq in freq_reached:
      freq_found = True
      break
    freq_reached.add(curr_freq)
  return curr_freq, freq_found

curr_freq = 0
freq_found = False

while not freq_found:
  curr_freq, freq_found = evaluate_all_changes(curr_freq)

print (curr_freq)