# Write a function that takes in a list & returns true if the number of items in that list is even (false otherwise).

# First understand the problem
# We want to write a function that takes in a list and return IF true so use an if else statement
# If you see that something takes in something - you'll probably need a parameter

my_list = [1,2,3,4,5]

def list_even(my_list):
  if (len(my_list) % 2 == 0):
    return True
  else:
    return False

print list_even(my_list)

# Refactored - the program will only get to line 22 if the condition was False

def list_even2(my_list):
  if (len(my_list) % 2 == 0):
    return True
  return False

print list_even2(my_list)

# Refactored again! Since the indented part is the true / false part we want, we can just return it and get the boolean

def list_even3(my_list):
  return len(my_list) % 2 == 0

print list_even3(my_list)
