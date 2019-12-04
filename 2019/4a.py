low = 356261
high = 846303
count = 0

def CountValidCombination(number):
  global count
  prev_digit = 99
  valid = False
  repeating_digit_count = 0

  while number > 0:
    digit = number % 10
    if prev_digit < digit:
      return
    elif prev_digit == digit:
      repeating_digit_count += 1
    else:
      if repeating_digit_count >= 2:
        valid = True
      repeating_digit_count = 1
    
    prev_digit = digit
    number = number / 10

  if valid or repeating_digit_count >= 2:
    count = count + 1
  return

map(CountValidCombination, range(low, high+1))
print (count)