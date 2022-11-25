# TITLE
# Multiply all elements in a list

# DESCRIPTION
# Write a Python program that multiplies all the items in a list by the value of the variable factor.
# The program must print the list as the output.
# The program should also allow multiplying the variable factor by a string in case the list contains strings.
# You may assume that the value of factor will be a positive integer.

# EXPECTED OUTPUT
# LIST              | FACTOR    | OUTPUT
# [3, 4, 5, 6]      | 2         | [6, 8, 10, 12]
# ["a", "b", "c"]   | 3         | ["aaa", "bbb", "ccc"]

# input_list = [3, 4, 5, 6]
# factor = 2

input_list = ["a", "b", "c"]
factor = 3

for i, elem in enumerate(input_list):
    input_list[i] = elem * factor

print(input_list)