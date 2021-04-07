# using a loop
def sum_squares(nums):
  total = 0
  for num in nums:
    total += num ** 2

  return total

# using built-in sum and a list comprehension
def sum_squares(nums):
  return sum([num ** 2 for num in nums])

# testing it
print(sum_squares([2, 2, 3])) # should be 17
