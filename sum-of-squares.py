def sum_of_square(array):
    total = 0
    for num in array:
        x = (num * num)
        total += x
    return total
    
print(sum_of_square([1, 2, 2]))