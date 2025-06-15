numbers = [3, 1, 4, 1, 5, 9, 2]


# What values do the following expressions have?

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = [1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = false
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#change first element to 10
numbers[0] = "ten"

# change the last element to 1
numbers[-1] = 1

#print all numbers, except last 2
print(numbers[2:])

#print wther 9 is an element of numbers
print(9 in numbers)

