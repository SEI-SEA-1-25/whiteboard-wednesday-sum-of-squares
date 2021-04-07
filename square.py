# Create a function that squares every number passed into it and then sums those squares together.

# For example, for [1, 2, 2] it should return 9, because 1^2 + 2^2 + 2^2 = 9.


def sum_squares(li):
  # keep a running total of the sum
  total = 0
  # squared array
  squares = []
  # loop over the incoming list
  for number in li:
    # appending the sqaure to a sqaure array
    # Math.pow(number, 2)
    # sqaures.append(number * number)
    squares.append(number ** 2)
  # loop over squares and sum them
  for square in squares:
    total += square
  # return the total
  return total


