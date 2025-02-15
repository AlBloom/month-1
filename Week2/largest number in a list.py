# Write a program to find the largest number in a list.
def maxnum (num):
  if not num:  # if the is empty
    return None

  return max(num)  

list = [] # Put any numbers you desire
MAX = maxnum (list)
print(MAX)
