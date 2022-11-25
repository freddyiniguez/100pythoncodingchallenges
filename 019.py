# TITLE
# Get Max and Min values

# DESCRIPTION
# Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, separated by a space.
# The largest value should appear first and the smallest value should appear second.
# You may assume that the list only contains numeric values.
# If the list is empty, print None.

# EXPECTED OUTPUT
# LIST              | OUTPUT
# [3, 4, 5, 6]      | 6 3
# [-1, -2, -3, -4]  | -1 -4
# [0, 0, 0, 0]      | 0 0
# []                | []

input_list = [3, 4, 5, 6]
# input_list = [-1, -2, -3, -4]
# input_list = [0, 0, 0, 0]
# input_list = []

if len(input_list) == 0:
    print(input_list)
else:
    print(f'{max(input_list)} {min(input_list)}')
