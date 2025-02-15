# Write a function that sums numbers in a list.

def sumnum (numbers):
  if not numbers:  # if the is empty
    return None
  return sum(numbers)
#The above is the whole function basically
# Now we call it

numbers = [] # you can add any numbers in this list for sumation
sums = sumnum(numbers)
print(sums)
