def sum_squares(nums):
  total = 0
  for num in nums:
    total += num ** 2

  return total

def sum_squares(nums):
  return sum([num ** 2 for num in nums])

print(sum_squares([2, 2, 3])) 