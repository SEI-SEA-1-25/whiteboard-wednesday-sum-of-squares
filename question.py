# // Create a function that squares every number passed into it and
# // then sums those squares together.

# // For example, for [1, 2, 2] it should return 9,
# // because 1^2 + 2^2 + 2^2 = 9.

# // Hints:
# // Don't forget that we're adding up all the squares,
# // NOT squaring the sum. For the above example, your result
# // should NOT be 25 (the square of the sum of 1, 2, and 2).
# // There are some ways to do this using python list comprehensions,
# // but a plain ol' for loop should do you fine!

def of_n_sum(integers):
    #set-up init total
    total = 0
    #loop through integers 
    for i in integers:
        #every loop adds (i to the power of 2)
        total += i ** 2
    return total

arr1 = [8, 6]
arr2 = [2, 3, 4]
# print(of_n_sum(arr1))