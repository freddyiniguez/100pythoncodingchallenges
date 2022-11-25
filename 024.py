# TITLE
# Count elements greater than 3

# DESCRIPTION
# Write a Python program that counts the number of elements in a list with value greater than 3.
# You may assume that the list only contains numbers.
# Print the final count.

# EXPECTED OUTPUT
# LIST                  | OUTPUT
# [1, -1, 0, 2, 2, 3]   | 0
# [1, 2, 3, 4]          | 1
# [7, 8, 9, 10]         | 4
# []                    | 0

input_list = [1, -1, 0, 2, 2, 3]
# input_list = [1, 2, 3, 4]
# input_list = [7, 8, 9, 10]
# input_list = []

greater_than_3 = 0

for i in input_list:
    if i > 3:
        greater_than_3 += 1

print(greater_than_3)

# Option:
# Solve this problem using a comprehension list
# greater_than_3 = sum(1 for i in input_list if i > 3)
